def hello():
  print("Hello World")

  hello()


  def pack(food1, food2, food3):
    print([food1, food2, food3])

    pack("turkey sandwich", "apple", "milk")


    def eat_lunch(food_list):
      if not food_list:
        print("First I eat", food_list[0])
        for i in food_list[1:]:
          print("Next I eat", i)
      else:
        print("My lunchbox is empty!")

    food_list = ["sandwich, apple, cookies, milk"]
    eat_lunch(food_list)
    eat_lunch([])
      