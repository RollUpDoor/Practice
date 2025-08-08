def main():
    dad = [
        " /‾‾‾‾‾‾\\",
        " |  O    O  |",
        " |     ∇    |",
        " |   \\___/  |",
        "  \\________/",
        "    |   |",
        "   /     \\",
        "   爸爸節快樂"
    ]

    for line in dad:
        print(line)


    dad_face = """
         (•_•)
         /|^|\\
          | |
         /   \\
         爸爸<3
       """

    print(dad_face*3)

    import time

    msg = " 爸爸88節快樂！"
    for i in range(8):
        print(msg[:i+1])
        time.sleep(0.2)

    import random

    eyes = ["o o", "O O", "•_•", "^ ^"]
    mouth = [" ^ ", " ~ ", " w ", "___"]
    beard = ["|||", "===", "^^^"]
    for i in range(5):
        e = random.choice(eyes)
        m = random.choice(mouth)
        b = random.choice(beard)
        print(f"  ({e})")
        print("  /|^|\\")
        print(f"   {m}")
        print(f"   {b}")
        print("  /   \\")
        print("  爸爸\n")


if __name__ == "__main__":
    main()
