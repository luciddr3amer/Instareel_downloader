# import instaloader

# # Create an instance of Instaloader
# L = instaloader.Instaloader()

# # URL of the Reels video to download
# url = "https://www.instagram.com/reel/CnM6XrroSFk/?utm_source=ig_web_copy_link"

# try:
#   # no video thumbnails
#     L.download_video_thumbnails = False
#     post = instaloader.Post.from_shortcode(L.context, url.split("/")[-2])

#     L.download_post(post, ".")
#     print("Reels video downloaded successfully!")
# except instaloader.exceptions.ProfileNotExistsException:
#     print("Invalid URL or the video is not available")
from flask import Flask, request, render_template, send_file
import os
import instaloader
import sys
import time
app = Flask(__name__)
download_loc=r'C:\Users\nijil\OneDrive\Desktop\newgit\downloads'

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == 'POST':
        url = request.form['url']
        L = instaloader.Instaloader()
        try:
            post = instaloader.Post.from_shortcode(L.context, url.split("/")[-2])
            L.download_video_thumbnails = False
            L.dirname_pattern = download_loc
            f=L.download_post(post, download_loc)
            return render_template('download.html')

        except instaloader.exceptions.ProfileNotExistsException:
            return "Invalid URL or the video is not available"
    return render_template('index.html')

def delete():
    for file in os.listdir(download_loc):
        if file.endswith('.mp4'):
             os.remove(os.path.join(download_loc, file))
    



@app.route('/download')
def download():
    for file in os.listdir(download_loc):
        if file.endswith('.mp4'):
            return send_file(os.path.join(download_loc, file), as_attachment=True)






 

  























        







if __name__ == '__main__':
    app.run(debug=True)


