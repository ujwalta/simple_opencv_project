import cv2

location = input("Enter the full path of the image: ").strip()

image = cv2.imread(location)

if image is not None:
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    user_input = input("Do you want to 'show' or 'save' the image? ").strip().lower()

    if user_input == "show":
        cv2.imshow("Original Image", image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        print("Original image is shown.")

    elif user_input == "save":
        file_name = input("Enter the name of the file to save (with extension, e.g., output.png): ").strip()
        cv2.imwrite(file_name, gray_image)
        print(f"Grayscale image saved as {file_name}")

    else:
        print("Invalid input. Please type 'show' or 'save'.")

else:
    print("Error: Could not load the image. Check the path and filename.")
