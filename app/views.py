from django.db.models.expressions import Value
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import JobSerializer, CandidateSerializer
from .models import Job, Candidate

#JobViews: represents the job endpoints 

class JobViews(APIView):
    #insert new job to the DB
    def post(self, request):
        serializer = JobSerializer(data={
            'title': request.data.get("title").lower(),
            'skills': [skill.lower() for skill in request.data.get("skills")] 
        })
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "job_id": serializer.data.get("id")}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    #return all jobs from the DB
    def get(self, request):
        if id:
            jobs = Job.objects.all().values()
            return Response({"status": "success", "data": jobs}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error"}, status=status.HTTP_400_BAD_REQUEST)


#CandidateViews: represents the candidate endpoints 

class CandidateViews(APIView):
    #insert new candidate to the DB
    def post(self, request):
        serializer = CandidateSerializer(data={
            'title': request.data.get("title").lower(),
            'skills': [skill.lower() for skill in request.data.get("skills")] 
        })
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "candidate_id": serializer.data.get("id")}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
    #return all candidates from the DB
    def get(self, request):
        if id:
            candidate = Candidate.objects.all().values()
            return Response({"status": "success", "data": candidate}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error"}, status=status.HTTP_400_BAD_REQUEST)


#CandidateFinderViews: represents the macth-candidate endpoints 

class CandidateFinderViews(APIView):
    #the core function - return list of macth candidate by job-id
    def get(self, request, job_id=None):
        if job_id:
            job = Job.objects.get(id=job_id)
            match_title =  Candidate.objects.all().filter(title = job.title)
            candidate_list = match_title.filter(skills__overlap=job.skills).values()
            
            #case there is no macthing skills between the job and the candidates - return matching by title
            if list(candidate_list) == [] or job.skills == []:
                best_match_list = match_title.values()
            
            #else - there is matching with title and skills
            else:
                best_match_list = candidate_finder(candidate_list, job.skills)

            return Response({"status": "success","candidate_list": best_match_list}, status=status.HTTP_200_OK)

        return Response({"status": "error", "data": "you should pass an id"}, status=status.HTTP_400_BAD_REQUEST)


def candidate_finder(candidate_list, job_skills):
    #check the number of the identical skills
    for candidate in candidate_list:
        candidate["match_skills"] = [skill for skill in candidate["skills"] if skill in job_skills]
        candidate["amount_match"] = len(candidate["match_skills"])
    sorted_candidate_list = sorted(candidate_list, key=lambda cand: cand["amount_match"], reverse=True)
    max_match = sorted_candidate_list[0].get("amount_match")
    best_match_list = []

    #return the candidate with the most identical skills
    for candidate in sorted_candidate_list:
        if candidate["amount_match"]==max_match:
            best_match_list.append({"id": candidate.get("id"),"title": candidate.get("title"), "skills": candidate.get("skills") })
        else:
            break

    return best_match_list