from audioop import reverse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic, decorators
from django.views.decorators.http import require_http_methods
from leave_request.forms import LeaveRequestForm
from leave_request.models import LeaveRequest
from django.contrib import messages
from django.contrib.auth.mixins  import LoginRequiredMixin
from django.http import HttpResponse

import csv, os

from .todos import todos

class LeaveRequestFormView(LoginRequiredMixin, generic.CreateView):
    template_name = 'leave_request/leave_request_form.html'
    form_class = LeaveRequestForm
    login_url = reverse_lazy('login')
    success_url = reverse_lazy('leave_request_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, 'Leave request submitted successfully')
        return super().form_valid(form)

class LeaveRequestDetailView(LoginRequiredMixin, generic.DetailView):
    login_url = reverse_lazy('login')
    model = LeaveRequest
    template_name = 'leave_request/leave_request_detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        todos = []
        context.update({"todos": todos})
        return context

class LeaveRequestListView(LoginRequiredMixin, generic.ListView):
    login_url = reverse_lazy('login')
    template_name = 'leave_request/leave_request_list.html'
    model = LeaveRequest

    def get_queryset(self):
        leave_requests = LeaveRequest.objects.filter(user=self.request.user)
        return leave_requests 

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        todos = []
        context.update({"todos": todos})
        return context
    
def get_doodles():
    data = []
    directory = os.getcwd()
    
    with open(f"{directory}/leave_request/doodles/list.csv", mode="r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        line_count = 0
        for row in csv_reader:
            line_count += 1
            data.append(
                {
                    "title": row["title"],
                    "date": f"{row['day']}/{row['month']}/{row['year']}",
                    "query": row["query"],
                    "url": row["url"],
                    "id": row["name"]
                })
    print(f"lines {line_count}")
        
    return data


    
def index(request):
    doodles = get_doodles()
    return render(request, 'leave_request/index.html', {'todos': [], "doodles": doodles})



@require_http_methods(['POST'])
def search(request):
    html = ""
    doodles = get_doodles()

    search = request.POST['search']
    print(search)

    for doodle in doodles:
        if search in doodle['title']:
            html += f"""
             <tr
    class="bg-white lg:hover:bg-gray-100 flex lg:table-row flex-row lg:flex-row flex-wrap lg:flex-no-wrap mb-10 lg:mb-0">
    <td class="w-full lg:w-auto p-3 text-gray-800 text-center border border-b block lg:table-cell relative lg:static">
      {doodle['date']}
    </td>
    <td class="w-full lg:w-auto p-3 text-gray-800 text-center border border-b block lg:table-cell relative lg:static">
        <a class="underline text-blue-500" href="{doodle['url']}">{doodle['title']}</a>
    </td>
    <td class="w-full lg:w-auto p-3 text-gray-800 text-center border border-b block lg:table-cell relative lg:static">
      {doodle["query"]}
    </td>
            """
    return HttpResponse(html)

def image(request):

    url =request.GET.get('url')
    print(url)
    image_url = url
    html = f"""<img src={image_url} />"""
    return HttpResponse(html)
