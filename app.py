from googletrans import Translator
from flask import Flask,render_template,request,redirect
from flask.ext.images import resized_img_src, Images
import numpy as np
from keras.preprocessing.image import ImageDataGenerator, img_to_array, load_img
from keras.models import Sequential
from keras.layers import Dropout, Flatten, Dense
from keras import applications
from keras.utils.np_utils import to_categorical
import matplotlib.pyplot as plt
import math
import cv2
import data
from bs4 import BeautifulSoup


app = Flask(__name__)

@app.route('/', methods=['POST','GET'])
def index():
   return render_template('index.html')

img_width, img_height = 224, 224
top_model_weights_path = 'insect_test_model.h5'
#train_data_dir = 'data/train'
#validation_data_dir = 'data/validation'
# epochs = 50
# batch_size = 16

d = {}
d[1] = 'rice leaf roller'
d[2] = 'rice leaf caterpillar'
d[4] = 'asiatic rice borer'
d[5] = 'yellow rice borer'
d[6] = 'rice gall midge'
d[7] = 'Rice Stemfly'
d[10] = 'small brown plant hopper'
d[11] = 'rice water weevil'
d[12] = 'rice leafhopper'
d[13] = 'grain spreader thrips'
d[14] = 'rice shell pest'
d[15] = 'grub'
d[16] = 'mole cricket'
d[19] = 'black cutworm'
d[20] = 'large cutworm'
d[21] = 'yellow cutworm' 
d[24] = 'army worm' 
d[25] = 'aphids'
d[26] = 'Potosiabre vitarsis'
d[37] = 'beet fly'


@app.route('/index2', methods = ['POST'])
def predict():
    if request.method == 'POST':
        a = request.form.to_dict()
        f = request.files['file']
        print("\n entered predict")
        class_dictionary = np.load('testinsectclass_indices.npy', allow_pickle=True).item()
        num_classes = len(class_dictionary)
        f.save('./static/'+f.filename)
        q = './static/'+f.filename  
        q1 = './static/'+f.filename
        print(q1)
        print("\n loaded image")
        image_path = q1
        orig = cv2.imread(image_path)

        print("[INFO] loading and preprocessing image...")
        image = load_img(image_path, target_size=(224, 224))
        image = img_to_array(image)

        image = image / 255

        image = np.expand_dims(image, axis=0)

        model = applications.VGG16(include_top=False, weights='imagenet')

        bottleneck_prediction = model.predict(image)

        model = Sequential()
        model.add(Flatten(input_shape=bottleneck_prediction.shape[1:]))
        model.add(Dense(256, activation='relu'))
        model.add(Dropout(0.5))
        model.add(Dense(num_classes, activation='sigmoid'))

        model.load_weights(top_model_weights_path)

        class_predicted = model.predict_classes(bottleneck_prediction)

        probabilities = model.predict_proba(bottleneck_prediction)

        inID = class_predicted[0]

        inv_map = {v: k for k, v in class_dictionary.items()}

        label = inv_map[inID]
        print("Image ID: {}, Label: {}".format(inID, label))
        avail = [12,4,6,21,10]
        translator = Translator()
        if int(label)-1 not in avail:  
            d[int(label)-1] = translator.translate(d[int(label)-1], dest=a['lang']).text
            iandd = translator.translate('Pest Indentification and Detailing', dest=a['lang'])
            resofp = translator.translate('Result of Pest Analysis', dest=a['lang'])
            nofp = translator.translate('Name of the Pest: ', dest=a['lang'])
            a = [iandd.text,resofp.text,nofp.text]
            return render_template('index2.html', result=d[int(label)-1], loc = f.filename, a=a)
        elif int(label)-1 == 12:
            d[int(label)-1] = translator.translate(d[int(label)-1], dest=a['lang'])
            iandd = translator.translate('Pest Indentification and Detailing', dest=a['lang'])
            resofp = translator.translate('Result of Pest Analysis', dest=a['lang'])
            nofp = translator.translate('Name of the Pest: ', dest=a['lang'])
            c = [iandd.text,resofp.text,nofp.text]
            a,b = data.greenlhop(a['lang'])
            return render_template('index3.html', result=d[int(label)-1].text, loc = f.filename, a=c, d=a, b=b)
        elif int(label)-1 == 6:
            d[int(label)-1] = translator.translate(d[int(label)-1], dest=a['lang'])
            iandd = translator.translate('Pest Indentification and Detailing', dest=a['lang'])
            resofp = translator.translate('Result of Pest Analysis', dest=a['lang'])
            nofp = translator.translate('Name of the Pest: ', dest=a['lang'])
            c = [iandd.text,resofp.text,nofp.text]
            a,b = data.gallmidge(a['lang'])
            return render_template('index3.html', result=d[int(label)-1].text, loc = f.filename, a=c, d=a, b=b)
        else:
            d[int(label)-1] = translator.translate(d[int(label)-1], dest=a['lang']).text
            iandd = translator.translate('Pest Indentification and Detailing', dest=a['lang'])
            resofp = translator.translate('Result of Pest Analysis', dest=a['lang'])
            nofp = translator.translate('Name of the Pest: ', dest=a['lang'])
            a = [iandd.text,resofp.text,nofp.text]
            return render_template('index2.html', result=d[int(label)-1], loc = f.filename, a=a)


@app.route('/purchase')
def purchase():
    return render_template('purchase.html')

@app.route('/purchase_result', methods=['POST','GET'])
def purchase_result():
    if request.method == 'POST':
        result = request.form.to_dict()
        a = result['state'].lower()
        if a == 'tamilnadu':
            a = 'timalnadu'
        elif ' ' in a:
            a = '-'.join(list(a.split(' ')))
        else:
            a = a
        b = result['city'].lower()
        c = result['sub'].lower()
        if ' ' in a:
            a = '-'.join(list(a.split(' ')))
        else:
            a = a
        url = 'https://www.napanta.com/fertilizer-dealer/'+a+'/'+b+'/'+c
        from bs4 import BeautifulSoup
        import requests
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        table = str(soup.findAll('td'))
        # print('\n'.join(table.split(', ')))
        a = '\n'.join(table.split(', '))
        a = a[1:len(a)-1]
        # print(a)
        a = a.replace('<td class="td-style">', '')
        # print(a)
        a = a.replace('</td>','')
        print(a)
        b = [['serial no','name','location']]
        a = a.split('\n')
        l = [a[0]]
        for i in range(1,len(a)):
            if a[i].isdigit() == True:
                b.append(l)
                l = []
                l.append(a[i])
            else:
                l.append(a[i])
        return render_template('purchase_result.html', b=b)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/sos')
def emergency():
    return render_template('emergency.html')

if __name__ == '__main__':
	app.run(debug=True)