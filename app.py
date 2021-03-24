from flask import Flask , render_template ,request
import os
import matplotlib.pyplot as plt
import image_style_transfer as ist

app = Flask(__name__)


@app.route('/')
def index():
    print("success")
    return render_template('index.html')

@app.route('/style',methods=['GET','POST'])
def style():
    style_img=request.files['style_file']
    content_img=request.files['content_file']
    style_img.save('static/style_img.jpg')
    content_img.save('static/content_img.jpg')
    style_path='static/style_img.jpg'
    content_path='static/content_img.jpg'
    best_img,best_loss=ist.run_style_transfer(content_path,style_path)
    plt.imsave('static/result.jpg',best_img)
    return render_template('style.html')
if __name__ =="__main__":
	app.run(debug=True)
