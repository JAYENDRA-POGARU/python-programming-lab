#variable length argument
def func(name,*fav_subjects):
    print("\n",name,"likes to read")
    for subject in fav_subjects:
        print(subject)
func("gorje","maths","c","python")
