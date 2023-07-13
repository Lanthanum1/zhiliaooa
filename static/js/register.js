function bindEmailCaptchaClick(){
  $("#captcha-btn").click(function (event){
    // $this：代表的是当前按钮的jquery对象
    var $this = $(this);
    // 阻止默认的事件
    event.preventDefault();
    const prefix = "http://127.0.0.1:5000"
    var email = $("input[name='email']").val();
    // console.log(prefix);
    $.ajax({

      // /auth/captcha/email?email=xx@qq.com
      url: prefix+"/auth/captcha/email?email="+email,

      method: "POST",
      success: function (result){
        var code = result['code'];
        if(code == 200){
          var countdown = 5;
          // 开始倒计时之前，就取消按钮的点击事件
          $this.off("click");
          var timer = setInterval(function (){
            console.log(countdown)
            $this.text(countdown);
            countdown -= 1;
            // 倒计时结束的时候执行
            if(countdown <= 0){
              // 清掉定时器
              clearInterval(timer);
              // 将按钮的文字重新修改回来
              $this.text("获取验证码");
              // 重新绑定点击事件
              bindEmailCaptchaClick();
            }
          }, 1000);
          // alert("邮箱验证码发送成功！");
        }else{
          alert(result['message']);
        }
      },
      fail: function (error){
        console.log(error);
      }
    })
  });
  $(document).ready(function() {
    $('#register-form').submit(function(event) {
        event.preventDefault();  // 阻止表单的默认提交行为

        var formData = $(this).serialize();  // 获取表单数据

        $.post('/register', formData, function(data) {
            if (data.error) {
                $('#error-message').text(data.error);  // 将错误信息显示到页面中的错误信息元素
                location.reload();  // 刷新页面
            } else {
                // 注册成功的逻辑
            }
        });
    });
});
}


// 整个网页都加载完毕后再执行的
$(function (){
  // alert("js test")
  bindEmailCaptchaClick();
});