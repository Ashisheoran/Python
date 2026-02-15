import threading
import os
from PIL import Image

INPUT_FOLDER = "input_images"
OUTPUT_FOLDER = "output_images"
os.makedirs(OUTPUT_FOLDER,exist_ok=True)

RESIZE_TO = (1000,1000)

def process_img(image_name):
    try:
        input_path = os.path.join(INPUT_FOLDER,image_name)
        output_path = os.path.join(OUTPUT_FOLDER,image_name)

        img = Image.open(input_path)
        img.resize(RESIZE_TO)
        img = img.convert('L')      # for gray scale
        img.save(output_path)

        print(f"Processed: {image_name}")
    except:
        print(f"Failed : {image_name}")

def main():
    images = [f for f in os.listdir(INPUT_FOLDER) if f.lower().endswith(('.png' , '.jpg' , '.jpeg'))]
    threads = []

    for image_name in images:
        t = threading.Thread(target=process_img,args=(image_name,))
        t.start()
        threads.append(t)
    for t in threads:
        t.join()

    print("\nAll images processed")

if __name__ == "__main__":
    main()