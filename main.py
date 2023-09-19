from flask import Flask
app = Flask(__name__)

@app.route("/")
def root():
    prefix_google = """
    <!-- Google tag (gtag.js) -->
    <script async
    src="https://www.googletagmanager.com/gtag/js?id=G-XKPPFHSPD4"></script>
    <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());
    gtag('config', ' G-XKPPFHSPD4');ls
    </script>
    """
    return prefix_google + "Hello from Space! 🚀"