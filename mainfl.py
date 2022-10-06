import os.path


from flask import Flask, request, render_template
from model.model import get_prediction
import torch


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])


def predict():
    UPLOAD_FOLDER = "static/"
    if request.method == "POST":
        file = request.files["image"]
        image_location = os.path.join(
            UPLOAD_FOLDER,
            file.filename)
        file.save(image_location)


        device = torch.device('cpu')
        PATH = './model/model_resnet18_weights.pth'

        model = torch.load(PATH, map_location=device)

        pred, prob_pred = get_prediction(file, model)

        return render_template('result1.html', prediction=pred,
                               proba=prob_pred, image_loc=file.filename)

    return render_template('result1.html', prediction=0, image_loc=None)


if __name__ == '__main__':

    app.run(debug=True, host='0.0.0.0', port=5000)

