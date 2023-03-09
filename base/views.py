from multiprocessing import context
from django.contrib import messages
import os
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from .models import Choice, Exam, Question, Score, SelectedChoice
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.views.decorators.cache import cache_control
from .forms import ExamForm, CreateQuestionForm
from .decorators import teacher_only, unauthenticated_user, allowed_users
from django.contrib.auth.models import Group
import datetime


# Create your views here.
# @allowed_users(allowed_roles=['teacher'])
# def tess(request):
#     return HttpResponse("you are here")

# @allowed_users(allowed_roles=['teacher'])
#-------------------------------------------------------

def tes(request):

    s = Score.objects.filter(exam__id=400)
    for i in s:
        print(i.user)

    context = {}
    #میانگین نمرات در امسال
    # end_date_year = datetime.datetime.now().date() + datetime.timedelta(days=1)
    # start_date_year = end_date_year + datetime.timedelta(days=-365)

    # this_year_exam = Score.objects.filter(user = request.user, created__range=[start_date_year, end_date_year])

    # number_of_this_year_this_user_exams = this_year_exam.count()

    # total_average_this_year = 0
    # total_scores_this_year = 0
    # for s in this_year_exam:
    #     total_scores_this_year = total_scores_this_year + s.score

    # if number_of_this_year_this_user_exams != 0:
    #     total_average_this_year = total_scores_this_year/number_of_this_year_this_user_exams

    # #میانگین نمرات در این ماه
    # end_date_month = datetime.datetime.now().date() + datetime.timedelta(days=1)
    # start_date_month = end_date_month + datetime.timedelta(days=-30)

    # # this_month_exam = Score.objects.filter(user = request.user, created__year=now_year, created__month=now_month)
    # this_month_exam = Score.objects.filter(user = request.user, created__range=[start_date_month, end_date_month])
    # # this_month_exam = Score.objects.filter(user = request.user, created__gte=datetime.date(2022, 11, 28), created__lte=datetime.date(2022, 12, 29))
    # # print(this_month_exam)

    # number_of_this_month_this_user_exams = this_month_exam.count()

    # total_average_this_month = 0
    # total_scores_this_month = 0
    # for s in this_month_exam:
    #     total_scores_this_month = total_scores_this_month + s.score

    # if number_of_this_month_this_user_exams != 0:
    #     total_average_this_month = total_scores_this_month/number_of_this_month_this_user_exams

    # #میانگین نمرات امروز

    # now_day = str(datetime.datetime.now().day)
    # now_month = str(datetime.datetime.now().month)
    # now_year = str(datetime.datetime.now().year)

    # today_exam = Score.objects.filter(user = request.user, created__year=now_year, created__month=now_month, created__day=now_day)

    # number_of_today_this_user_exams = today_exam.count()

    # total_average_today = 0
    # total_scores_today = 0
    # for s in today_exam:
    #     total_scores_today = total_scores_today + s.score

    # if number_of_today_this_user_exams != 0:
    #     total_average_today = total_scores_today/number_of_today_this_user_exams

    # #میانگین نمرات کل
    # exam = Score.objects.filter(user = request.user)

    # number_of_all_this_user_exams = exam.count()
    # # print(number_of_all_this_user_exams)

    # total_average = 0
    # total_scores = 0
    # for s in exam:
    #     total_scores = total_scores + s.score

    # if number_of_all_this_user_exams != 0:
    #     total_average = total_scores/number_of_all_this_user_exams


    # context = {"exam": exam,
    #             "total_average": total_average,
    #             "total_average_this_month": total_average_this_month,
    #             "total_average_this_year": total_average_this_year,
    #             "number_of_this_year_this_user_exams": number_of_this_year_this_user_exams,
    #             "number_of_this_month_this_user_exams": number_of_this_month_this_user_exams,
    #             "number_of_all_this_user_exams": number_of_all_this_user_exams,
    #             "total_average_today": total_average_today,
    #             "number_of_today_this_user_exams": number_of_today_this_user_exams
    #             }
    
    return render(request, 'base/tes.html', context)
    # form = CreateUserForm()
    # if form.is_valid():
    #     user = form.save()
    #     username = form.cleaned_data.get('username')

    #     group = Group.objects.get(name='student')
    #     user.groups.add(group)
    #     messages.success(request, 'Lalalallaalla')
    # context = {'form':form}
#-------------------------------------------------------


    # messages.error(request, 'Lalalalallaal')

    # context = {}
    # return render(request, 'base/tes.html', context)

# def averages(request):
    
#     #میانگین نمرات در امسال
#     end_date_year = datetime.datetime.now().date() + datetime.timedelta(days=1)
#     start_date_year = end_date_year + datetime.timedelta(days=-365)

#     this_year_exam = Score.objects.filter(user = request.user, created__range=[start_date_year, end_date_year])

#     number_of_this_year_this_user_exams = this_year_exam.count()

#     total_average_this_year = 0
#     total_scores_this_year = 0
#     for s in this_year_exam:
#         total_scores_this_year = total_scores_this_year + s.score

#     if number_of_this_year_this_user_exams != 0:
#         total_average_this_year = total_scores_this_year/number_of_this_year_this_user_exams

#     #میانگین نمرات در این ماه
#     end_date_month = datetime.datetime.now().date() + datetime.timedelta(days=1)
#     start_date_month = end_date_month + datetime.timedelta(days=-30)

#     # this_month_exam = Score.objects.filter(user = request.user, created__year=now_year, created__month=now_month)
#     this_month_exam = Score.objects.filter(user = request.user, created__range=[start_date_month, end_date_month])
#     # this_month_exam = Score.objects.filter(user = request.user, created__gte=datetime.date(2022, 11, 28), created__lte=datetime.date(2022, 12, 29))
#     print(this_month_exam)

#     number_of_this_month_this_user_exams = this_month_exam.count()

#     total_average_this_month = 0
#     total_scores_this_month = 0
#     for s in this_month_exam:
#         total_scores_this_month = total_scores_this_month + s.score

#     if number_of_this_month_this_user_exams != 0:
#         total_average_this_month = total_scores_this_month/number_of_this_month_this_user_exams

#     #میانگین نمرات کل
#     exam = Score.objects.filter(user = request.user)

#     number_of_all_this_user_exams = exam.count()
#     # print(number_of_all_this_user_exams)

#     total_average = 0
#     total_scores = 0
#     for s in exam:
#         total_scores = total_scores + s.score

#     if number_of_all_this_user_exams != 0:
#         total_average = total_scores/number_of_all_this_user_exams


#     context = {
#                 "total_average": total_average,
#                 "total_average_this_month": total_average_this_month,
#                 "total_average_this_year": total_average_this_year,
#                 "number_of_this_year_this_user_exams": number_of_this_year_this_user_exams,
#                 "number_of_this_month_this_user_exams": number_of_this_month_this_user_exams,
#                 "number_of_all_this_user_exams": number_of_all_this_user_exams
#                 }
#     return render(request, 'base/profile.html', context)


def home(request):
    context = {}
    return render(request, 'base/home.html', context)

@login_required(login_url='base:login')
@teacher_only
def create_question(request):
    # form = CreateQuestionForm()
    # if request.method == 'POST':
    #     form = CreateQuestionForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         messages.success(request, 'Question created')

            # return redirect('base/create_question.html')

    # context = {'form': form}
    if request.method == 'POST':
        if request.POST.get(("save_next")):
            question = request.POST.get('question')
            correct_choice = request.POST.get('correct_choice')
            choice2 = request.POST.get('choice2')
            choice3 = request.POST.get('choice3')
            choice4 = request.POST.get('choice4')
            
            if question == "":
                messages.error(request, "question field can not be empty!!")
            elif correct_choice == "":
                messages.error(request, "Correct choice field can not be empty!!")
            elif choice2 == "" and choice3 == "" and choice4 == "":
                messages.error(request, "At least 2 choices are needed!!")
            else:
                question_instance = Question.objects.create(question_text = question)
                question_instance.save()
                print(question_instance.id)
                correct_choice_instance = Choice.objects.create(question_id=question_instance.id, choice_text=correct_choice, correct=True)
                correct_choice_instance.save()
                if choice2 != "":
                    choice_instance2 = Choice.objects.create(question_id=question_instance.id, choice_text=choice2, correct=False)
                    choice_instance2.save()
                if choice3 != "":
                    choice_instance3 = Choice.objects.create(question_id=question_instance.id, choice_text=choice3, correct=False)
                    choice_instance3.save()
                if choice4 != "":
                    choice_instance4 = Choice.objects.create(question_id=question_instance.id, choice_text=choice4, correct=False)
                    choice_instance4.save()
                messages.success(request, "Question added successfully.")
                messages.success(request, "You can add another.")



        if request.POST.get("save_home"):
            question = request.POST.get('question')
            correct_choice = request.POST.get('correct_choice')
            choice2 = request.POST.get('choice2')
            choice3 = request.POST.get('choice3')
            choice4 = request.POST.get('choice4')
            
            if question == "":
                messages.error(request, "question field can not be empty!!")
            elif correct_choice == "":
                messages.error(request, "Correct choice field can not be empty!!")
            elif choice2 == "" and choice3 == "" and choice4 == "":
                messages.error(request, "At least 2 choices are needed!!")
            else:
                question_instance = Question.objects.create(question_text = question)
                question_instance.save()
                print(question_instance.id)
                correct_choice_instance = Choice.objects.create(question_id=question_instance.id, choice_text=correct_choice, correct=True)
                correct_choice_instance.save()
                if choice2 != "":
                    choice_instance2 = Choice.objects.create(question_id=question_instance.id, choice_text=choice2, correct=False)
                    choice_instance2.save()
                if choice3 != "":
                    choice_instance3 = Choice.objects.create(question_id=question_instance.id, choice_text=choice3, correct=False)
                    choice_instance3.save()
                if choice4 != "":
                    choice_instance4 = Choice.objects.create(question_id=question_instance.id, choice_text=choice4, correct=False)
                    choice_instance4.save()            
                return redirect('base:home')


    context = {}
    return render(request, 'base/create_question.html', context)

@login_required(login_url='base:login')
def exams(request):
    exams = Exam.objects.all()
    context = {'exams': exams}
    return render(request, 'base/exams.html', context)
    
@login_required(login_url='base:login')
def exam(request, pk):
    sc = ""
    try:
        sc = Score.objects.get(user=request.user, exam_id=pk)
    except:
        pass
    if sc:
        context = {'pk': pk}
        return render(request, 'base/exam_block.html', context)
        # questions = Question.objects.all()
        # username = request.user.username
        # # for question in questions:
        # #     exam.question.add(question)
        
        # # print(questions[0].choice_set.all())
        # context = {'questions': questions, 'username':username, 'sc': sc}
    else:
        username = request.user.username
        questions = Exam.objects.get(id=pk).question.all()
        score = 0
        from_20 = 0
        total = len(questions)
        if request.method == 'POST':
            for q in questions:

                # print(q.choice_set.get(id=request.POST[q.question_text]).correct)
                try:
                    selected_choice = q.choice_set.get(id=request.POST[str(q.id)])
                    this_question = Question.objects.get(id=q.id)
                    s = SelectedChoice.objects.create(
                        selectedChoice_text = selected_choice,
                        user = request.user,
                        question = this_question
                    )

                    if selected_choice.correct == True:
                        score += 1
                    #     correct += 1
                    # else:
                    #     wrong += 1
                    try:
                        from_20 = (score/total)*20
                    except:
                        pass

                    e = Exam.objects.get(id=pk)
                    s.exam.add(e)
                    # selects = SelectedChoice.objects.filter(user=request.user, exam_id=pk)
                except:
                    pass
                
                # selected_choice.selected_choice.selected_choice = selected_choice
                # selected_choice.save()


            e = Exam.objects.get(id=pk)
            sco = Score.objects.create(user=request.user, exam=e)
            sco.score = from_20
            sco.save()
            return redirect(request.path_info)
        

        context = {
            "username": username,
            "questions": questions,

        }


        return render(request, 'base/exam.html', context)

@login_required(login_url='base:login')
def result(request, pk):
    username = request.user.username
    try:
        exam = Exam.objects.get(id=pk)
        questions = exam.question.all()
        from_20 = Score.objects.get(user=request.user, exam=exam).score
    except:
        return HttpResponse("Not found !!!")
    correct = 0
    wrong = 0
    score = 0
    total = len(questions)
    selected_choice = SelectedChoice.objects.filter(user=request.user, exam=pk)
    
    # if Score.objects.get(user=request.user, exam=exam) is None:
    #     return HttpResponse("Not found!!")

    for selected in selected_choice:
        # if selected.selectedChoice_text ==
        for choice in selected.question.choice_set.all():
            # print(choice.choice_text)
            # print(selected.selectedChoice_text)
            if choice.choice_text == selected.selectedChoice_text:
                if choice.correct is True:
                    correct += 1
                    score += 1
                else:
                    wrong += 1

    #معدل کل در این آزمون
    this_exam = Score.objects.filter(exam__id= pk)
    number_of_all_users = this_exam.count()

    total_average_this_exam = 0
    total_scores_this_exam = 0
    for s in this_exam:
        total_scores_this_exam = total_scores_this_exam + s.score

    if number_of_all_users != 0:
        total_average_this_exam = total_scores_this_exam/number_of_all_users

    context = {
        "questions": questions,
        "username": username,
        "exam": exam,
        "pk": pk,
        "selected_choice": selected_choice,
        "from_20": from_20,
        "score": score,
        "correct": correct,
        "wrong": wrong,
        "total": total,
        "total_average_this_exam": total_average_this_exam,
        "number_of_all_users": number_of_all_users,
        }
    return render(request, 'base/result.html', context)

            # print(q.choice_set.get(id=request.POST[q.question_text]).correct)
            # print(request.POST[])
    
    
@login_required(login_url='base:login')
@teacher_only
def addQuestion(request):
    if request.method == 'POST':
        # module_dir = os.path.dirname(__file__)  
        # file_path = os.path.join(module_dir, 'files/fifth-task-exam.txt')   #full path to text.
        # data_file = open(file_path , 'r')       
        # data = data_file.read()
        try:
            data = request.FILES.get('myfile').read()
            data = data.decode("utf-8")
            print(data)
            question_list = []
            the_list = []
            the_index = 0
            q = data.split("\\")
            for item in q:
                the_list.append(item)
                if the_index % 2 == 1:
                    the_list.append(0)
                    question_list.append(the_list)
                    the_list = []
                the_index += 1

            print(question_list)
            grade = 0

            for item in question_list:

                questionsAndAnswers = item[0].splitlines( )
                questionsAndAnswers = list(filter(None, questionsAndAnswers))

                print(questionsAndAnswers)
                question = questionsAndAnswers[0]
                # question_instance = Question.objects.create(id=Question.objects.all().count() + 1, question_text = question)
                question_instance = Question.objects.create(question_text = question)
                question_instance.save()

                a = questionsAndAnswers[1]
                b = questionsAndAnswers[2]
                c = questionsAndAnswers[3]
                d = questionsAndAnswers[4]

                if item[1]=="A":
                    o = Choice.objects.create(question_id=question_instance.id, choice_text=a, correct=True)
                    o = Choice.objects.create(question_id=question_instance.id, choice_text=b, correct=False)
                    o = Choice.objects.create(question_id=question_instance.id, choice_text=c, correct=False)
                    o = Choice.objects.create(question_id=question_instance.id, choice_text=d, correct=False)
                elif item[1]=="B":
                    o = Choice.objects.create(question_id=question_instance.id, choice_text=a, correct=False)
                    o = Choice.objects.create(question_id=question_instance.id, choice_text=b, correct=True)
                    o = Choice.objects.create(question_id=question_instance.id, choice_text=c, correct=False)
                    o = Choice.objects.create(question_id=question_instance.id, choice_text=d, correct=False)            
                elif item[1]=="C":
                    o = Choice.objects.create(question_id=question_instance.id, choice_text=a, correct=False)
                    o = Choice.objects.create(question_id=question_instance.id, choice_text=b, correct=False)
                    o = Choice.objects.create(question_id=question_instance.id, choice_text=c, correct=True)
                    o = Choice.objects.create(question_id=question_instance.id, choice_text=d, correct=False)
                elif item[1]=="D":
                    o = Choice.objects.create(question_id=question_instance.id, choice_text=a, correct=False)
                    o = Choice.objects.create(question_id=question_instance.id, choice_text=b, correct=False)
                    o = Choice.objects.create(question_id=question_instance.id, choice_text=c, correct=False)
                    o = Choice.objects.create(question_id=question_instance.id, choice_text=d, correct=True)
            messages.success(request, "Questions successfuly added!")

        except:
            messages.error(request, "Something went wrong!!")

#-----------------------------------------------------------------------------------------------------------------------

        # question_instance2 = Question.objects.get_or_create(question_text = "2 + 3 + 4?")
        # print(question_instance2[0].id)

        # news_obj = Question.objects.get(id=question_instance2[0].id)
        # question_instance = Question.objects.create(id=Question.objects.all().count() + 1, question_text = "2 + 2 + 4?")
        # question_instance.save()
        # question_instance=question_instance[0].id
        # print(question_instance.id)
        # something1 = "Something 1"
        # something4 = "Something 4"
        # print(news_obj)
        # o = Choice.objects.create(id=Choice.objects.all().count() + 1, question_id=question_instance.id, choice_text=something1, correct=True)

        # o = Choice.objects.get_or_create(id=Choice.objects.all().count() + 1, question_id=question_instance.id, choice_text=something4, correct=False)

        # o.save()
    context={}
    return render(request, "base/addQuestion.html", context)

def loginPage(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('base:home')
        
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist!')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('base:home')
        else:
            messages.error(request, 'Username OR Password is invalid!')

    context = {'page': page}
    return render(request, "base/login_register.html", context)

def registerUser(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            group = Group.objects.get(name='student')
            user.groups.add(group)
            login(request, user)
            return redirect('base:home')
        else:
            messages.error(request, "Something went wrong during registeration!!")

    context = {'form': form}
    return render(request, "base/login_register.html", context)

def logoutUser(request):
    logout(request)
    return redirect('base:home')

@login_required(login_url='base:login')
@teacher_only
def createExam(request):
    form = ExamForm()
    
    if request.method == 'POST':
        form = ExamForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('base:home')

    context = {'form': form}
    return render(request, "base/create_exam.html", context)

@login_required(login_url='base:login')
def profileUser(request):

    #میانگین نمرات در امسال
    end_date_year = datetime.datetime.now().date() + datetime.timedelta(days=1)
    start_date_year = end_date_year + datetime.timedelta(days=-365)

    this_year_exam = Score.objects.filter(user = request.user, created__range=[start_date_year, end_date_year])

    number_of_this_year_this_user_exams = this_year_exam.count()

    total_average_this_year = 0
    total_scores_this_year = 0
    for s in this_year_exam:
        total_scores_this_year = total_scores_this_year + s.score

    if number_of_this_year_this_user_exams != 0:
        total_average_this_year = total_scores_this_year/number_of_this_year_this_user_exams

    #میانگین نمرات در پارسال
    end_date_last_year = datetime.datetime.now().date() + datetime.timedelta(days=-364)
    start_date_last_year = end_date_year + datetime.timedelta(days=-730)

    last_year_exam = Score.objects.filter(user = request.user, created__range=[start_date_last_year, end_date_last_year])

    number_of_last_year_this_user_exams = last_year_exam.count()

    total_average_last_year = 0
    total_scores_last_year = 0
    for s in last_year_exam:
        total_scores_last_year = total_scores_last_year + s.score

    if number_of_last_year_this_user_exams != 0:
        total_average_last_year = total_scores_last_year/number_of_last_year_this_user_exams

    #میانگین نمرات در این ماه
    end_date_month = datetime.datetime.now().date() + datetime.timedelta(days=1)
    start_date_month = end_date_month + datetime.timedelta(days=-30)

    # this_month_exam = Score.objects.filter(user = request.user, created__year=now_year, created__month=now_month)
    this_month_exam = Score.objects.filter(user = request.user, created__range=[start_date_month, end_date_month])
    # this_month_exam = Score.objects.filter(user = request.user, created__gte=datetime.date(2022, 11, 28), created__lte=datetime.date(2022, 12, 29))

    number_of_this_month_this_user_exams = this_month_exam.count()

    total_average_this_month = 0
    total_scores_this_month = 0
    for s in this_month_exam:
        total_scores_this_month = total_scores_this_month + s.score

    if number_of_this_month_this_user_exams != 0:
        total_average_this_month = total_scores_this_month/number_of_this_month_this_user_exams

    #میانگین نمرات در ماه قبل
    end_date_last_month = datetime.datetime.now().date() + datetime.timedelta(days=-29)
    start_date_last_month = end_date_month + datetime.timedelta(days=-60)

    # this_month_exam = Score.objects.filter(user = request.user, created__year=now_year, created__month=now_month)
    last_month_exam = Score.objects.filter(user = request.user, created__range=[start_date_last_month, end_date_last_month])
    # this_month_exam = Score.objects.filter(user = request.user, created__gte=datetime.date(2022, 11, 28), created__lte=datetime.date(2022, 12, 29))

    number_of_last_month_this_user_exams = last_month_exam.count()

    total_average_last_month = 0
    total_scores_last_month = 0
    for s in last_month_exam:
        total_scores_last_month = total_scores_last_month + s.score

    if number_of_last_month_this_user_exams != 0:
        total_average_last_month = total_scores_last_month/number_of_last_month_this_user_exams


    #میانگین نمرات امروز

    now_day = str(datetime.datetime.now().day)
    now_month = str(datetime.datetime.now().month)
    now_year = str(datetime.datetime.now().year)

    today_exam = Score.objects.filter(user = request.user, created__year=now_year, created__month=now_month, created__day=now_day)

    number_of_today_this_user_exams = today_exam.count()

    total_average_today = 0
    total_scores_today = 0
    for s in today_exam:
        total_scores_today = total_scores_today + s.score

    if number_of_today_this_user_exams != 0:
        total_average_today = total_scores_today/number_of_today_this_user_exams

    #میانگین نمرات کل
    exams = Score.objects.filter(user = request.user)

    number_of_all_this_user_exams = exams.count()
    # print(number_of_all_this_user_exams)

    total_average = 0
    total_scores = 0
    for s in exams:
        total_scores = total_scores + s.score

    if number_of_all_this_user_exams != 0:
        total_average = total_scores/number_of_all_this_user_exams

    #میانگین همه نمرات کل شرکت کنندگان

    #امسال
    end_date_year_all = datetime.datetime.now().date() + datetime.timedelta(days=1)
    start_date_year_all = end_date_year + datetime.timedelta(days=-365)

    this_year_exam_all = Score.objects.filter(created__range=[start_date_year, end_date_year])

    number_of_this_year_exams = this_year_exam_all.count()

    total_average_this_year_all = 0
    total_scores_this_year_all = 0
    for s in this_year_exam_all:
        total_scores_this_year_all = total_scores_this_year_all + s.score

    if number_of_this_year_exams != 0:
        total_average_this_year_all = total_scores_this_year_all/number_of_this_year_exams

    #این ماه
    end_date_month_all = datetime.datetime.now().date() + datetime.timedelta(days=1)
    start_date_month_all = end_date_month + datetime.timedelta(days=-30)

    this_month_exam_all = Score.objects.filter(created__range=[start_date_month, end_date_month])
    # this_month_exam = Score.objects.filter(user = request.user, created__gte=datetime.date(2022, 11, 28), created__lte=datetime.date(2022, 12, 29))

    number_of_this_month_exams = this_month_exam_all.count()

    total_average_this_month_all = 0
    total_scores_this_month_all = 0
    for s in this_month_exam_all:
        total_scores_this_month_all = total_scores_this_month_all + s.score

    if number_of_this_month_exams != 0:
        total_average_this_month_all = total_scores_this_month_all/number_of_this_month_exams

    #امروز

    now_day = str(datetime.datetime.now().day)
    now_month = str(datetime.datetime.now().month)
    now_year = str(datetime.datetime.now().year)

    today_exam_all = Score.objects.filter(created__year=now_year, created__month=now_month, created__day=now_day)

    number_of_today_exams = today_exam_all.count()

    total_average_today_all = 0
    total_scores_today_all = 0
    for s in today_exam_all:
        total_scores_today_all = total_scores_today_all + s.score

    if number_of_today_exams != 0:
        total_average_today_all = total_scores_today_all/number_of_today_exams

    #میانگین نمرات کل
    exams = Score.objects.all()

    number_of_all_exams = exams.count()

    total_average_all = 0
    total_scores_all = 0
    for s in exams:
        total_scores_all = total_scores_all + s.score

    if number_of_all_exams != 0:
        total_average_all = total_scores_all/number_of_all_exams
#-------------------------------------------------------------------

    includeList = []
    exceptList = []
    user = request.user

    score = Score.objects.filter(user=request.user)
    for item in score:
        includeList.append(item.exam)

    exam = Exam.objects.all()
    for item in exam:
        if item not in includeList:
            exceptList.append(item)
    num5 = 5
    num11 = 11
    context = {
        'exam': exam,
        'exceptList': exceptList,
        'user': user,
        'score': score,
        "total_average": total_average,
        "total_average_this_month": total_average_this_month,
        "total_average_this_year": total_average_this_year,
        "number_of_this_year_this_user_exams": number_of_this_year_this_user_exams,
        "number_of_this_month_this_user_exams": number_of_this_month_this_user_exams,
        "number_of_all_this_user_exams": number_of_all_this_user_exams,
        "total_average_today": total_average_today,
        "number_of_today_this_user_exams": number_of_today_this_user_exams,
        
        "total_average_this_year_all": total_average_this_year_all,
        "total_average_this_month_all": total_average_this_month_all,
        "total_average_today_all": total_average_today_all,
        "total_average_all": total_average_all,

        "total_average_last_year": total_average_last_year,
        "number_of_last_year_this_user_exams": number_of_last_year_this_user_exams,
        "total_average_last_month": total_average_last_month,
        "number_of_last_month_this_user_exams": number_of_last_month_this_user_exams,

    }
    return render(request, 'base/profile.html', context)

@login_required(login_url='base:login')
@teacher_only
def add_and_create_questions(request):
    context = {}
    return render(request, 'base/add_and_create_questions.html', context)

@login_required(login_url='base:login')
@teacher_only
def exams_list(request):

    exams = Exam.objects.all()

    context = {"exams": exams}
    return render(request, 'base/exams_list.html', context)

def results_exams(request, pk):
    score = ""
    exam = ""
    try:
        score = Score.objects.filter(exam_id=pk)
    except:
        messages.error(request, "Nobody have performed this exam yet!")
    
    try:
        exam = Exam.objects.get(id=pk)
    except:
        messages.error(request, "This exam does not exist!")

    context = {"score": score, "exam": exam}
    return render(request, 'base/results_exams.html', context)