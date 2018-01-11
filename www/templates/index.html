<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
    <form action="/csrf" method="post">
        {% raw xsrf_form_html() %}
        <p><input name="user" type="text" placeholder="用户"/></p>
        <p><input name='pwd' type="text" placeholder="密码"/></p>
        <input type="submit" value="Submit" />
        <input type="button" value="Ajax CSRF" onclick="SubmitCsrf();" />
    </form>
    
    <script src="/statics/jquery-1.12.4.js"></script>
    <script type="text/javascript">

        function ChangeCode() {
            var code = document.getElementById('imgCode');
            code.src += '?';
        }
        function getCookie(name) {
            var r = document.cookie.match("\\b" + name + "=([^;]*)\\b");
            return r ? r[1] : undefined;
        }

        function SubmitCsrf() {
            var nid = getCookie('_xsrf');
            $.post({
                url: '/csrf',
                data: {'k1': 'v1',"_xsrf": nid},
                success: function (callback) {
                    // Ajax请求发送成功有，自动执行
                    // callback，服务器write的数据 callback=“csrf.post”
                    console.log(callback);
                }
            });
        }
    </script>
</body>
</html>
