from django.core.management.base import BaseCommand
from movies.models import Movie, Person, Gener, Occupation
import pickle 
import datetime
import re

from recom_me.settings import base


class Command(BaseCommand):
    def handle(self, *args, **options):
        FILE_NAME = base.BASE_DIR + '/movie_movies_data.pickle'
        # Load the dictionary back from the pickle file.
        print(base.BASE_DIR)
        data_list = pickle.load(open(FILE_NAME, "rb"))
        
        for data in data_list:
            try:
                title = re.sub("[\(\[].*?[\)\]]", "",data['film_name']['value']).strip() 
            except:
                title = None
            try:
                value = data['film_director']['value']
                if ',' in value :
                    director_list = value.split(',')
                else:
                    director_list = []
                    director_list.append(value) 
            except:
                director_list = None
            try:
                value = data['film_writer']['value']
                if ',' in value :
                    writer_list = value.split(',')
                else:
                    writer_list = []
                    writer_list.append(value)
            except:
                writer_list = []
            try:
                value = data['actor_name']['value']
                if ',' in value :
                    actor_list = value.split(',')
                else:
                    actor_list = []
                    actor_list.append(value)     
            except:
                actor_list = []
            try:
                value = data['film_producer']['value']
                if ',' in value :
                    producer_list = value.split(',')
                else:
                    producer_list = []
                    producer_list.append(value)
            except:
                producer_list = []
            try:
                value = data['film_screenplay']['value']
                if ',' in value :
                    screenplay_list = value.split(',')
                else:
                    screenplay_list = []
                    screenplay_list.append(value)
            except:
                screenplay_list = []
            editing_list = []
            try:
                value = data['film_editing']['value']
                if ',' in value :
                    editing_list = value.split(',')
                else:
                    editing_list = []
                    editing_list.append(value)
            except:
                editing_list = []

            try:
                value = data['film_cinematography']['value']
                if ',' in value :
                    cinematography_list = value.split(',')
                else:
                    cinematography_list = []
                    cinematography_list.append(value)
            except:
                cinematography_list = []
            
            try:
                value = data['film_musicComposers']['value']
                if ',' in value :
                    musicComposers_list = value.split(',')
                    
                else:
                    musicComposers_list = []
                    musicComposers_list.append(value)
            except:
                musicComposers_list = []
            try:
                description_list = data['film_abstract']['value']
            except:
                description_list = []
            try:
                wikiPageUrl_list = "https://en.wikipedia.org/wiki/index.html?curid=" + data['film_wikiPageID']['value']
            except:
                wikiPageUrl_list = []


            # mlist = Movie(titel = title , directors = director_list, writers = writer_list, 
            #           actors = actor_list, producer = producer_list, 
            #           screenplay = screenplay_list, editing = editing_list,
            #           cinematography = cinematography_list, musicComposers = musicComposers_list,
            #           description = description_list, wikiPageUrl = wikiPageUrl_list
            #   )
            if not Movie.objects.filter(title__iexact = title).exists():
                mlist = Movie(title = title , 
                          description = description_list, wikiPageUrl = wikiPageUrl_list
                  )
                mlist.save()
            else: 
                mlist= Movie.objects.get(title = title)
            
            for d in director_list:
                if not Person.objects.filter(fullname__iexact = d).exists():
                    try:
                        d.split(' ')[1]
                    except:
                        continue
                    if len(d.split(' ')) == 2 :
                        p = Person(fullname=d, firstname=d.split(' ')[0], lastname=d.split(' ')[1])
                        p.save()
                        o_object = Occupation.objects.get(title = 'director')
                        p.occupations.add(o_object)
                    elif len(d.split(' ')) > 2 :
                else:
                    dp = Person.objects.get(fullname = d)
                    mlist.directors.add(dp)

            for w in writer_list:
                if not Person.objects.filter(fullname__iexact = w).exists():
                    try:
                        w.split(' ')[1]
                    except:
                        continue
                    p = Person(fullname=w, firstname=w.split(' ')[0], lastname=w.split(' ')[1])
                    p.save()
                    o_object = Occupation.objects.get(title = 'writer')
                    p.occupations.add(o_object)
                else:
                    wp = Person.objects.get(fullname = w)
                    mlist.writers.add(wp)

            for a in actor_list:
                if not Person.objects.filter(fullname__iexact = a).exists():
                    try:
                        a.split(' ')[1]
                    except:
                        continue
                    p = Person(fullname=a, firstname=a.split(' ')[0], lastname=a.split(' ')[1])
                    p.save()
                    o_object = Occupation.objects.get(title = 'actor')
                    p.occupations.add(o_object)
                else:
                    pass
                    #ap = Person.objects.get(fullname = a)
                    #mlist.actors(ap)

            for p in producer_list:
                if not Person.objects.filter(fullname__iexact = p).exists():
                    try:
                        p.split(' ')[1]
                    except:
                        continue
                    pe = Person(fullname=p, firstname=p.split(' ')[0], lastname=p.split(' ')[1])
                    pe.save()
                    o_object = Occupation.objects.get(title = 'producer')
                    pe.occupations.add(o_object)
                else:
                    pp = Person.objects.get(fullname = p)
                    print(pp)
                    mlist.producers.add(pp)

            for s in screenplay_list:
                if not Person.objects.filter(fullname__iexact = s).exists():
                    try:
                        s.split(' ')[1]
                    except:
                        continue
                    p = Person(fullname=s, firstname=s.split(' ')[0], lastname=s.split(' ')[1])
                    p.save()
                    o_object = Occupation.objects.get(title = 'screenplay')
                    p.occupations.add(o_object)
                else:
                    sp = Person.objects.get(fullname = s)
                    mlist.screenplays.add(sp)

            for e in editing_list:
                if not Person.objects.filter(fullname__iexact = e).exists():
                    try:
                        e.split(' ')[1]
                    except:
                        continue
                    p = Person(fullname=e, firstname=e.split(' ')[0], lastname=e.split(' ')[1])
                    p.save()
                    o_object = Occupation.objects.get(title = 'editing')
                    p.occupations.add(o_object)
                else:
                    ep = Person.objects.get(fullname = e)
                    mlist.editing.add(ep)

            for c in cinematography_list:
                if not Person.objects.filter(fullname__iexact = c).exists():
                    try:
                        c.split(' ')[1]
                    except:
                        continue
                    p = Person(fullname=c, firstname=c.split(' ')[0], lastname=c.split(' ')[1])
                    p.save()
                    o_object = Occupation.objects.get(title = 'cinematography')
                    p.occupations.add(o_object)
                else:
                    cp = Person.objects.get(fullname = c)
                    mlist.cinematography.add(cp)

            for m in musicComposers_list:
                if not Person.objects.filter(fullname__iexact = m).exists():
                    try:
                        m.split(' ')[1]
                    except:
                        continue
                    p = Person(fullname=m, firstname=m.split(' ')[0], lastname=m.split(' ')[1])
                    p.save()
                    o_object = Occupation.objects.get(title = 'music composer')
                    p.occupations.add(o_object)
                else:
                    mp = Person.objects.get(fullname = m)
                    mlist.musicComposers.add(mp)


            # try:
            #     first_name = data['person_givenname']['value'].strip()
            # except:
            #     first_name = '-'
            # try:
            #     last_name = data['person_surname']['value'].strip()
            # except:
            #     last_name = '-'
            # try:
                
            #     full_name = re.sub("[\(\[].*?[\)\]]", "",data['person_name']['value']).strip()
            #     #full_name = first_name + " " + last_name
            # except:
            #     fullname = '-'

            # try:
            #     gender_label = data['gender_label']['value']
            #     if gender_label == "Female":
            #         gender_label = 'F'
            #     elif gender_label == "Male":
            #         gender_label = "M"
            #     print(gender_label)
            # except:
            #     gender_label = None
            # occupation_list =[]
            # try:
            #     # there was occupation like actor,producer and also http://.../musician
            #     occ = data['person_occupation']['value']

            #     if ',' in occ:
            #         occ_list = occ.split(',')
            #     if 'http:' in occ:
            #         occ_list = []
            #         occ_list.append(occ.split('/')[-1])
            #     for occupation in occ_list:
            #         occupation_list.append(occupation.lower())
            #         #print(occupation_list)
            # except:
            #     pass
            # try:
            #     DOB = data['person_DOB']['value']
            #     datetime.datetime.strptime(DOB, '%Y-%m-%d')
            # except:
            #     DOB = None
            # try:
            #     POB = data['person_POB']['value']
            # except:
            #     POB = None
            # try:
            #     bio = data['person_abstract']['value']
            # except:
            #     bio = None
            # try:
            #     wikiPageID = data['person_wikiPageID']['value']
            # except:
            #     wikiPageID = None
            # try:
            #     nationality = data['person_nationality']['value']
            # except:
            #     nationality = None
            # # occupation_list = Occupation.objects.filter(title = occupation)
            # if not occupation_list:
            #     if not Person.objects.filter(fullname__iexact = full_name).exists():
            #             p = Person(fullname=full_name, firstname = first_name , lastname=last_name , gender=gender_label ,
            #                 date_of_birth=DOB, place_of_birth= POB, nationality = nationality, wikiPediaPage_ID= wikiPageID,
            #                 biography= bio
            #              )
            #             p.save()
                       
            #     else:
            #         pass
            # for occupation in occupation_list:
            #     if not Occupation.objects.filter(title = occupation).exists() and not occupation.isspace():
            #         o = Occupation(title = occupation)
            #         o.save()
            #         if not Person.objects.filter(fullname__iexact = full_name).exists():
            #             p = Person(fullname=full_name, firstname = first_name , lastname=last_name , gender=gender_label ,
            #                 date_of_birth=DOB, place_of_birth= POB, nationality = nationality, wikiPediaPage_ID= wikiPageID,
            #                 biography= bio
            #              )
            #             p.save()
            #             p.occupations.add(o)
            #         else:
            #             p = Person.objects.get(fullname__iexact = full_name)
            #             p.occupations.add(o)
            #             p.save()
            #     elif not occupation.isspace(): 
            #         if not Person.objects.filter(fullname__iexact = full_name).exists() :
            #             p = Person(fullname=full_name, firstname = first_name , lastname=last_name , gender=gender_label ,
            #                 date_of_birth=DOB, place_of_birth= POB, nationality = nationality, wikiPediaPage_ID= wikiPageID,
            #                 biography= bio
            #              )
            #             p.save()
            #             o_object = Occupation.objects.get(title = occupation)
            #             p.occupations.add(o_object)
            #         else:
            #             o = Occupation.objects.get(title = occupation)
            #             p = Person.objects.get(fullname__iexact = full_name)
            #             p.occupations.add(o)
            #             p.save()
            
    # def handle(self, *args, **options):
 #        self._saveDataFromFile()





