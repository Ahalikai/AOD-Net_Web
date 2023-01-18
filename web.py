#! _*_ coding: utf-8 _*_

import os


from flask import make_response
from flask import request
from PIL import Image
from flask import Flask, send_from_directory
from Algorithm import dehaze, PicSimilar

def create_app(test_config=None):
    # 创建和配置应用程序
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'baby.sqlite')
    )

    if test_config is None:
        # 加载实例配置（如果存在），不测试时
        app.config.from_pyfile('config.py', silent=True)
    else:
        # 如果传入则加载测试配置
        app.config.from_mapping(test_config)

    # 确保实例文件夹存在
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # 一个简单的页面
    #@app.route('/hello')
    @app.route('/')
    def index():
        return 'Hello, World!'




    @app.route("/<path:filename>")
    def getImages(filename):
        image_path1 = filename
        image_path2 = dehaze.dehaze.dehaze_image(image_path1)
        #image1 = Image.open(image_path1)

        similar = PicSimilar.similar(image_path1, image_path2)
        print('%.2f%%' % (similar * 100) )

        result_z = " "
        if(similar > 0.2):
            result_z = result_z + "红色预警"
        elif(similar > 0.08):
            result_z = result_z + "橙色预警"
        elif(similar > 0.02):
            result_z = result_z + "黄色预警"
        else:
            result_z = result_z + "天气晴朗"

        #result_z = result_z + ' (相似度：' + similar + ')\n'
        result_z = result_z + "(STD：" + (str)( '%.2f%%' % (similar * 100) ) + ")\n"
        print(result_z)
        #return filename
        return result_z
        #return send_from_directory(dirpath, filename, as_attachment=True)

    return app

application = create_app()

if __name__ == "__main__":
    application.run()
