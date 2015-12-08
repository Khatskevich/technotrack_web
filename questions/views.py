from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic import ListView
from answer.forms import NewAnswerForm
from answer.models import Answer
from questions.forms import NewQuestionForm
from questions.models import Question
from django.contrib.auth.decorators import login_required


class QuestionsAll(ListView):
    def get_queryset(self):
        if 'sort' in self.request.GET.keys():
            if self.request.GET['sort']=='title':
                return Question.get_query_sorted_by_title()
            if self.request.GET['sort']=='date':
                return Question.get_query_sorted_by_publish_date()
            if self.request.GET['sort']=='likes':
                return Question.get_query_sorted_by_likes()
        return Question.objects.all()
    model = Question
    paginate_by = '15'
    context_object_name = "questions"
    template_name='search.html'
    def get_context_data(self):
        context = super(QuestionsAll, self).get_context_data()
        context['user_id']=self.request.user.pk
        return context


def NewQuestion(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/login/')
    if request.method == 'POST':
        form = NewQuestionForm(request.POST)
        if form.is_valid():
            question = Question()
            question.user=request.user
            question.title = form.cleaned_data['title']
            question.text = form.cleaned_data['text']
            question.save()
            print "Ok"
            return HttpResponseRedirect('/question/'+str(question.pk)+'/')
        else:
            return render_to_response('new_question.html', {'form': form}, context_instance=RequestContext(request))
    else:
        ''' '''
        form = NewQuestionForm()
        context = {'form':form}
        return  render_to_response('new_question.html',context, context_instance=RequestContext(request))

def QuestionView(request, pk):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/login/')
    if request.method == 'POST':
        form = NewAnswerForm(request.POST)
        if form.is_valid():
            answer = Answer()
            answer.text=form.cleaned_data['text']
            answer.title=form.cleaned_data['title']
            answer.user = request.user
            answer.question=Question.objects.get(pk=int(pk))
            answer.save()
            print "Ok"
            send_mail('Subject', 'You have new answers', 'avkhatskevich@gmail.com',
                      ['lesaha.95@mail.ru'], fail_silently=False)
            return HttpResponseRedirect('/question/'+pk+'/#answer'+str(answer.pk))
        else:
            context = {'form':form}
            context['question']= Question.objects.get(pk=int(pk))
            context['answers']= Answer.objects.filter(question__pk=int(pk))
            return render_to_response('question.html', context, context_instance=RequestContext(request))
    else:
        ''' '''
        form = NewAnswerForm()
        context = {'form':form}
        context['question']= Question.objects.get(pk=int(pk))
        context['answers']= Answer.objects.filter(question__pk=int(pk))
        return  render_to_response('question.html',context, context_instance=RequestContext(request))