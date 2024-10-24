from FactorioBlueprintMaker.Generator import FactorioBlueprintGenerator
from VideoConverter.videoConverter import convert


def main():
    gif_file_path = input("Enter file path: ")

    resize = input("Need resize? [Y/N]: ")
    if resize.lower() == "y" or resize.lower() == "yes":
        resize = int(input("Enter new height (MAX=2161): "))
    else: resize = None

    fps = input("Need change fps? [Y/N]: ")
    if fps.lower() == "y" or fps.lower() == "yes":
        fps = int(input("Enter new fps: "))
    else: fps = None

    data = convert(gif_file_path, height=resize, fps=fps)

    data = FactorioBlueprintGenerator(data).generate()

    with open("blueprint.txt", "w") as f:
        f.write(data)

    print("Your blueprint done!")


if __name__ == "__main__":
    main()