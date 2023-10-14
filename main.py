from flask import Flask
import logging

app = Flask(__name__)


@app.route('/', methods=["GET"])
def hello_world():
    pre = """
<!-- Google tag (gtag.js) -->
<script async
src="https://www.googletagmanager.com/gtag/js?id=G-WEKFJ1L7K3"></script>
<script>
window.dataLayer = window.dataLayer || [];
function gtag(){dataLayer.push(arguments);}
gtag('js', new Date());
gtag('config', 'G-XKPPFHSPD4');
</script>
"""

    tag_manager = """
<!-- Google Tag Manager -->
<script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
})(window,document,'script','dataLayer','GTM-5K8NHJ4');</script>
<!-- End Google Tag Manager -->
"""

    button = """
<button>
    Dams's Button
</button>
"""
    return pre + tag_manager + "Hello World" + button


@app.route('/logger', methods=["GET"])
def logger_page():
    page = """
    <script>
    console.log('This is a front-end log');
    </script>


    <script>
    alert('Text is in a text box');
    </script>
    """

    print('This is a back-end log')
    return page + "This page logs stuff"
