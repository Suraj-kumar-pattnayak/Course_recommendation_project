class CourseInfo:
    def __init__(self, course_id, rating):
        self.course_id = course_id
        self.rating = rating
class UserInfo:
    def __init__(self, user_id, user_choice):
        self.user_id = user_id
        self.user_choice = user_choice
        

tot_user = input("enter how many users completed some courses: ")
user_info = []
def dataset():
    for i in range(int(tot_user)):
        u_id = input("enter user id: ")
        u_choice = []
        tot_cour = input("enter total number of courses done by this user: ")
        for j in range(int(tot_cour)):
            curr_cour = input("enter course: ")
            curr_rating = input("enter that course rating: ")
            u_choice.append(CourseInfo(curr_cour, curr_rating))
        user_info.append(UserInfo(u_id, u_choice))

def matching(id):
    match_score = []
    for i in range(int(50)):
        match_score.append(0)
    res_course = []
    for user in user_info:
        if user.user_id == id:
            res_course = user.user_choice
    for cour in res_course:
        count = 0
        for user in user_info:
            if user.user_id == id:
                count += 1
                continue
            else:
                for other_cour in user.user_choice:
                    if cour.course_id == other_cour.course_id:
                        match_score[count] += 1
                count += 1
    return match_score
        

dataset()

    
opinion = input("Are you want to chhose a course? yes/no: ")
while opinion.lower() == "yes":
    for user in user_info:
        user.user_choice = sorted(user.user_choice, key=lambda x: x.rating, reverse=True )
    id = input("enter your user id: ")
    exist_id = False
    self_idx = 0
    for user in user_info:
        self_idx = self_idx+1
        if user.user_id == id:
            exist_id = True
            break
    if exist_id:
        match_score = matching(id)
        max_value = max(match_score)
        max_idx = match_score.index(max_value)
        # print('your matching user at idx: ',max_idx)
        # self_idx = match_score.index(0) +1
        self_idx = self_idx - 1
        # print('and you are at index: ',self_idx)
        print("your id is exist in online learning platform!")
        for match_course in user_info[max_idx].user_choice:
            course_done = False
            for first_user_course in user_info[self_idx].user_choice:
                if match_course.course_id == first_user_course.course_id:
                    course_done = True
            if not(course_done):
                print("recommended course to you is: ",match_course.course_id)
                ans = input("Are you interested to choose that course? yes/no: ")
                if ans.lower() == "no":
                    curr_cour = input("enter your course name that to be choosed: ")
                    curr_cour_rat = input("enter rating of that course: ")
                    user_info[self_idx].user_choice.append(CourseInfo(curr_cour, curr_cour_rat))
                    break
                elif ans.lower() == "yes":
                    recom_cour_rat = input("enter your rating to that course: ")
                    user_info[self_idx].user_choice.append(CourseInfo(match_course.course_id, recom_cour_rat))
                    break
                else:
                    print('invalid answer!')
                    break
    else:
        u_id = id
        u_choice = []
        tot_cour = input("enter total number of courses done by this user: ")
        for j in range(int(tot_cour)):
            curr_cour = input("enter course: ")
            curr_rating = input("enter that course rating: ")
            u_choice.append(CourseInfo(curr_cour, curr_rating))
        user_info.append(UserInfo(u_id, u_choice))

    opinion = input("Are you want to choose a course? yes/no: ")


