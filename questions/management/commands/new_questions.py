# -*- coding: utf-8 -*-
from random import random, randint
from django.core.management import BaseCommand
from answer.models import Answer
from questions.models import Question

titles = [
    'How do I heal a broken heart?',
    'Why do I never see baby pigeons?',
    'I dont understand how Lost ended.',
    'Am I pretty?',
    'Why won’t my wife listen to me?',
    'What are your strengths?',
    'What are your weaknesses?',
    'Why should we hire you?',
    'What can you do for us that other candidates cant?',
    'Where do you see yourself in five years time?',
    'Why do you want to work here?',
    'What are three positive things your last boss would say about you?',
    'What salary are you seeking?',
    'If you were an animal, which one would you want to be?',
    'Navy Yard Shooting – Who was the Navy Yard shooter?',
    'Oscar Pistorius – Did Oscar Pistorium kill his girlfriend?',
    'Ariel Castro – Who did Ariel Castro kidnap?',
    'Detroit Bankruptcy – How far in debt is Detroit?',
    'Benedict XVI – Why did Pope Benedict step down?',
    'Syrian – Will the U.S. invade Syria?',
]
questions = [
    "This is usually the opening question and, as first impressions are key, one of the most important. Keep your answer to under five minutes, beginning with an overview of your highest qualification then running through the jobs you’ve held so far in your career. You can follow the same structure of your CV, giving examples of achievements and the skills you’ve picked up along the way. Don't go into too much detail – your interviewer will probably take notes and ask for you to expand on any areas where they'd like more information. If you're interviewing for your first job since leaving education, focus on the areas of your studies you most enjoyed and how that has led to you wanting this particular role.",
    "Pick the three biggest attributes that you think will get you the job and give examples of how you have used these strengths in a work situation. They could be tangible skills, such as proficiency in a particular computer language, or intangible skills such as good man-management. If you're not sure where to start, take a look at the job description. There is usually a section listing candidate requirements, which should give you an idea of what they are looking for.",
    "The dreaded question, which is best handled by picking something that you have made positive steps to redress. For example, if your IT ability is not at the level it could be, state it as a weakness but tell the interviewer about training courses or time spent outside work hours you have used to improve your skills. Your initiative could actually be perceived as a strength. On no accounts say I don’t have any weaknesses, your interviewer won't believe you, or I have a tendency to work too hard, which is seen as avoiding the question.",
    "It's best to talk about both short-term and long-term goals. Talk about the kind of job you'd eventually like to do and the various steps you will need to get there, relating this in some way back to the position you're interviewing for. Show the employer you have ambition, and that you have the determination to make the most of every job you have to get where you want to be.",
    "The interviewer is listening for an answer that indicates you've given this some thought. If you've prepared for the interview properly, you should have a good inside knowledge of the company's values, mission statement, development plans and products. Use this information to describe how your goals and ambition matches their company ethos and how you would relish the opportunity to work for them. ",
    "This is a great time to brag about yourself through someone else's words. Try to include one thing that shows your ability to do the job, one thing that shows your commitment to the work, and one thing that shows you are a good person to have in a team. ",
    "You can prepare for this by knowing the value of someone with your skills. Try not to give any specific numbers in the heat of the moment – it could put you in a poor position when negotiating later on. Your interviewer will understand if you don't want to discuss this until you are offered the job. If they have provided a guideline salary with the job description, you could mention this and say it's around the same area you’re looking for.",
    "Interviewers use this type of psychological question to see if you can think quickly. If you answer 'a bunny', you will make a soft, passive impression. If you answer 'a lion', you will be seen as aggressive. What type of personality will it take to get the job done?",
    "You should always have some questions for your interviewer to demonstrate your interest in the position. Prepare a minimum of five questions, some which will give you more information about the job, and some which delve deeper into the culture and goals of the company.",
    "For Christ died for sins once for all, the righteous for the unrighteous, to bring you to God. He was put to death in the body but made alive by the Spirit, through whom also he went and preached to the spirits in prison.",
    "Typically, when an algorithm is associated with processing information, data are read from an input source, written to an output device, and/or stored for further processing. Stored data are regarded as part of the internal state of the entity performing the algorithm. In practice, the state is stored in one or more data structures.",
    "For some such computational process, the algorithm must be rigorously defined: specified in the way it applies in all possible circumstances that could arise. That is, any conditional steps must be systematically dealt with, case-by-case; the criteria for each case must be clear (and computable).",
    "Because an algorithm is a precise list of precise steps, the order of computation is always critical to the functioning of the algorithm. Instructions are usually assumed to be listed explicitly, and are described as starting from the top and going down to the bottom, an idea that is described more formally by flow of control.",
]
images = [
    '1.jpg',
    '2.jpg',
    '3.jpg',
    '4.jpg','5.jpg',
    '6.jpg','7.jpg',
    '8.jpg','9.jpg',
    '10.jpg','11.jpg',
    '12.jpg','13.jpg',
    '14.jpg','15.jpg',
    '16.jpg','17.jpg',
]

class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int)

    def handle(self, *args, **options):
        count = options['count']
        for answer in Answer.objects.all():
            answer.delete()
        for question in Question.objects.all():
            question.delete()
        for i in range(0, count):
            number = randint(0,len(titles)-1)
            question = Question()
            question.title = titles[ number ]
            question.likes = 0
            number = randint(0,len(questions)-1)
            question.text = questions[ number ]
            number = randint(0,len(images)-1)
            question.image_url = images[ number]
            question.save()
            for j in range(0,randint(0,5)):
                answer = Answer()
                number = randint(0,len(questions)-1)
                answer.text = questions[number]
                number = randint(0,len(titles)-1)
                answer.title = titles[ number ]
                answer.question = question
                answer.save()

