print("Importing Necessary Modules...")
start = __import__('time').time()
import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
import time
from tensorflow import keras
from tensorflow.keras.models import load_model
from PIL import Image
import os
print(f"Modules imported within \033[94m{time.time() - start} seconds\033[0m.")
val_accs = []


class CustomCallback(tf.keras.callbacks.Callback):
    def __init__(self, model_save):
        if model_save[-1] != "/":
            model_save = model_save + "/"
        self.model_location = model_save

    def on_epoch_end(self, epoch, logs=None):
        current_epoch = epoch + 1

        current_training_accuracy = logs['accuracy']
        current_testing_accuracy = logs['val_accuracy']

        current_training_loss = logs['loss']
        current_testing_loss = logs['val_loss']

        global val_accs
        val_accs.append(current_testing_accuracy)

        print(f" | val_loss: {current_testing_loss} - val_accuracy: {current_testing_accuracy}")

        self.model.save(f'{self.model_location}my_model_with_val_acc_{current_training_accuracy}.keras')


def train_model(EPOCHs: int = 500, model_saving_location=""):
    mnist = tf.keras.datasets.mnist
    (x_train, y_train), (x_test, y_test) = mnist.load_data()

    print(f"{len(x_train)} {len(x_test)}")
    print(f"{x_train.shape} {x_test.shape}")

    print(f"{len(y_train)} {len(y_test)}")
    print(f"{y_train.shape} {y_test.shape}")

    # Normalizing the Data
    x_train = x_train / 255
    x_test = x_test / 255

    # Defining the Model
    model = keras.Sequential([
        keras.layers.Reshape((28, 28, 1), input_shape=(28, 28)),
        keras.layers.Conv2D(32, (3, 3), activation='relu'),
        keras.layers.MaxPooling2D((2, 2)),
        keras.layers.Conv2D(64, (3, 3), activation='relu'),
        keras.layers.MaxPooling2D((2, 2)),
        keras.layers.Conv2D(64, (3, 3), activation='relu'),
        keras.layers.Flatten(),
        keras.layers.Dense(64, activation='relu'),
        keras.layers.Dense(512, activation='relu'),
        keras.layers.Dropout(0.2),
        keras.layers.Dense(256, activation='relu'),
        keras.layers.Dropout(0.2),
        keras.layers.Dense(128, activation='relu'),
        keras.layers.Dropout(0.2),
        keras.layers.Dense(62, activation='softmax')
    ])

    # Compiling the Model
    model.compile(optimizer='sgd', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

    # Training the Model
    history = model.fit(x_train, y_train, validation_data=(x_test, y_test), epochs=EPOCHs, callbacks=[CustomCallback(model_saving_location)])

    history.history.keys()
    plt.plot(history.history['accuracy'])
    plt.plot(history.history['val_accuracy'])
    plt.title('model accuracy')
    plt.ylabel('accuracy')
    plt.xlabel('epoch')
    plt.legend(['Train', 'Validation'], loc='upper left')
    plt.show()

    plt.plot(history.history['loss'])
    plt.plot(history.history['val_loss'])
    plt.title('model loss')
    plt.ylabel('loss')
    plt.xlabel('epoch')
    plt.legend(['Train', 'Validation'], loc='upper left')
    plt.show()

    plt.plot(history.history['accuracy'])
    plt.plot(history.history['val_accuracy'])
    plt.plot(history.history['loss'])
    plt.plot(history.history['val_loss'])
    plt.title('Training Loss and accuracy')
    plt.ylabel('accuracy/Loss')
    plt.xlabel('epoch')
    plt.legend(['accuracy', 'val_accuracy', 'loss', 'val_loss'])
    plt.show()


def processing_image(model_name_: str = "my_model_with_val_acc_1.keras", images: tuple = (), saving_loc: str = ""):
    try:
        print("Loading Model")
        model_ = load_model(model_name_)
        print("Model Loaded...")

    except Exception as e:
        print("No Model Found with the given Testing Accuracy !")
        print("Error:", e)
        return

    # Processing the Input Image
    for image_path in images:
        img = Image.open(image_path).convert('L')
        img = img.resize((28, 28))
        img_arr = np.array(img)
        img_arr = img_arr / 255.0
        img_arr = img_arr.reshape(1, 28, 28)

        # Predict the handwritten character in the image
        predicted_value = model_.predict(img_arr)

        # Print the predicted value

        print(f"Handwritten number in the image '{image_path}' is '%d'" % np.argmax(predicted_value))
        plt.imshow(img)
        plt.suptitle(f"Handwritten number in the below image is '%d'" % np.argmax(predicted_value))
        img_name = image_path.split("/")[-1]
        plt.savefig(f'{saving_loc+img_name}')
        plt.show()


def main():
    try:
        if not os.path.exists(img_pathway):  # or (not os.path.exists(model_pathway)) or (not os.path.exists(result_saving_loc)) or (not os.path.exists("val_acc_logs")):
            exit(f"Location '{img_pathway}' not found ! ")
        elif not os.path.exists(model_pathway):
            exit(f"Location '{model_pathway}' not found ! ")
        elif not os.path.exists(result_saving_loc):
            exit(f"Location '{result_saving_loc}' not found ! ")
        elif not os.path.exists(log_file):
            exit(f"Log file '{log_file}' not found ! ")
        elif (EPOCHS == 0) and (already_trained in [0, False, None]):
            exit(f"Unable to train with {EPOCHS = } ! ")
        else:
            print("Requirements satisfied ! ")
        if already_trained:
            model_name = f"my_model_with_val_acc_{max([float(x) for x in open(log_file, 'r').readlines()])}.keras"
            model_name = model_pathway + model_name
            imgs_set = tuple(f"{img_pathway + f}" for f in os.listdir(img_pathway) if os.path.isfile(os.path.join(img_pathway, f)) and os.path.splitext(f)[1] in ['.png', '.jpg', '.jpeg', '.bmp', '.tiff'])
            processing_image(model_name_=model_name, images=imgs_set, saving_loc=result_saving_loc)
        else:
            train_model(EPOCHs=EPOCHS, model_saving_location=model_pathway)
            with open(log_file, 'a') as file:
                file.write(str(max(val_accs)) + "\n")
    except KeyboardInterrupt:
        exit("Terminating ...")
    except:
        print("Some Error Occurred ! ")


if __name__ == "__main__":
    ###################################################  Custom_Variables  ####################################################
    already_trained = True                                                                                                   ##
    img_pathway, model_pathway, result_saving_loc, log_file, EPOCHS = "Images/", "Models/", "Results/", "val_acc_logs", 500  ##
    ###########################################################################################################################
    main()
