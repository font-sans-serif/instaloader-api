from flask import Flask, request, jsonify
import instaloader

app = Flask(__name__)
L = instaloader.Instaloader()

@app.route("/reel")
def get_reel_info():
    shortcode = request.args.get("shortcode")
    if not shortcode:
        return jsonify({"error": "Missing shortcode"}), 400
    try:
        post = instaloader.Post.from_shortcode(L.context, shortcode)
        return jsonify({
            "video_url": post.video_url,
            "caption": post.caption,
            "author": post.owner_username
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/")
def home():
    return "🟢 Instaloader API is running."

if __name__ == "__main__":
    app.run()