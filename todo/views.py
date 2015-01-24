from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.http import Http404
from models import Todo


def todolist(request):
    username = request.COOKIES.get('username','')
    todolist = Todo.objects.filter(flag=1).filter(user=username)
    finishtodos = Todo.objects.filter(flag=0).filter(user=username)
    return render_to_response('todo/simpleTodo.html',
                              {'todolist': todolist,
                                  'finishtodos': finishtodos,
                                  'username': username},
                              context_instance=RequestContext(request))


def wancheng(request):
    username = request.COOKIES.get('username', '')
    print 'wancheng'
    try:
        id = request.GET['id']
        print id
        todo = Todo.objects.get(id=id)
    except Exception:
        raise Http404
    if todo:
        if todo.flag == 1:
            todo.flag = 0
            todo.save()
            todolist = Todo.objects.filter(flag=1).filter(user=username)
            finishtodos = Todo.objects.filter(flag=0).filter(user=username)
            return render_to_response('todo/showtodo.html',
                                      {'todolist': todolist,
                                          'finishtodos': finishtodos
                                          },
                                      context_instance=RequestContext(request))
    else:
        return HttpResponseRedirect('/todo/')


def todoback(request, id=''):
    username = request.COOKIES.get('username', '')
    todo = Todo.objects.get(id=id)
    if todo.flag == 0:
        todo.flag = 1
        todo.save()
        return HttpResponseRedirect('/todo/')
    todolist = Todo.objects.filter(flag=1).filter(user=username)
    return render_to_response('todo/simpleTodo.html', {'todolist': todolist,'username': username},
                              context_instance=RequestContext(request))



def addtodo(request):
    username = request.COOKIES.get('username', '')
    print 'add'
    if request.method == 'POST':
        print 'post'
        atodo = request.POST['todo']
        priority = request.POST['priority']
        todo = Todo(user=username,todo=atodo, priority=priority, flag=1)
        todo.save()
        todolist = Todo.objects.filter(flag=1).filter(user=username)
        finishtodos = Todo.objects.filter(flag=0).filter(user=username)
        return render_to_response('todo/showtodo.html',
                                  {'todolist': todolist,
                                   'finishtodos': finishtodos
                                   },
                                  context_instance=RequestContext(request))
    else:
        todolist = Todo.objects.filter(flag=1).filter(user=username)
        finishtodos = Todo.objects.filter(flag=0).filter(user=username)
        return render_to_response('todo/simpleTodo.html',
                                  {'todolist': todolist, 'finishtodos': finishtodos,'username': username})



def todoshanchu(request):
    username = request.COOKIES.get('username', '')
    print 'shanchu'
    try:
        id = request.GET.get('id')
        print id
        todo = Todo.objects.get(id=id)
    except Exception:
        raise Http404
    if todo:
        todo.delete()
        todolist = Todo.objects.filter(flag=1).filter(user=username)
        finishtodos = Todo.objects.filter(flag=0).filter(user=username)
        return render_to_response('todo/showtodo.html',
                                  {'todolist': todolist,
                                      'finishtodos': finishtodos
                                      },
                                  context_instance=RequestContext(request))
    else:
        todolist = Todo.objects.filter(flag=1).filter(user=username)
        finishtodos = Todo.objects.filter(flag=0).filter(user=username)
        return render_to_response('todo/simpleTodo.html',
                                  {'todolist': todolist, 'finishtodos': finishtodos,'username': username})


def todoupdate(request):
    username = request.COOKIES.get('username', '')
    print 'update'
    if request.method == 'POST':
        try:
            id = request.POST['id']
            todo = Todo.objects.get(id=id)
        except Exception:
            raise Http404

        todo.todo = request.POST['todo']
        todo.priority = request.POST['priority']
        print 'pp'+'todo.priority'
        todo.save()
        todolist = Todo.objects.filter(flag=1).filter(user=username)  
        finishtodos = Todo.objects.filter(flag=0).filter(user=username)
        return render_to_response('todo/showtodo.html',
                                  {'todolist': todolist,
                                      'finishtodos': finishtodos,
                                      },
                                  context_instance=RequestContext(request))
    try:
        id = request.GET.get('id')
        print id
        todo = Todo.objects.get(id=id)
    except Exception:
        raise Http404
        print 'error'
    if todo:
        return render_to_response('todo/updatatodo.html', {'todo': todo},
                                  context_instance=RequestContext(request))
    else:
        todolist = Todo.objects.filter(flag=1).filter(user=username)
        finishtodos = Todo.objects.filter(flag=0).filter(user=username)
        return render_to_response('todo/simpleTodo.html',
                                  {'todolist': todolist, 'finishtodos': finishtodos})


#backup def
def todofinish(request, id=''):
    username = request.COOKIES.get('username', '')
    todo = Todo.objects.get(id=id)
    if todo.flag == 1:
        todo.flag = 0
        todo.save()
        return HttpResponseRedirect('/todo/')
    todolist = Todo.objects.filter(flag=1).filter(user=username)
    return render_to_response('todo/simpleTodo.html', {'todolist': todolist,'username':username},
                              context_instance=RequestContext(request))


#backup def
def updatetodo(request, id=''):
    username = request.COOKIES.get('username', '')
    try:
        todo = Todo.objects.get(id=id)
    except Exception:
        raise Http404
    if request.method == 'POST':
        print 'ddd'
        todo.todo = request.POST['todo']
        todo.priority = request.POST['priority']
        todo.save()
        todolist = Todo.objects.filter(flag=1).filter(user=username)
        finishtodos = Todo.objects.filter(flag=0).filter(user=username)
        return render_to_response('todo/simpleTodo.html',
                                  {'todolist': todolist,
                                      'finishtodos': finishtodos,
                                      'username':username},
                                  context_instance=RequestContext(request))
    else:
        try:
            todo = Todo.objects.get(id=id)
        except Exception:
            raise Http404
        return render_to_response('todo/updatatodo.html', {'todo': todo},
                                  context_instance=RequestContext(request))

#backup def
def deletetodo(request, id=''):
    username = request.COOKIES.get('username', '')
    try:
        todo = Todo.objects.get(id=id)
    except Exception:
        raise Http404
    if todo:
        todo.delete()
        return HttpResponseRedirect('/todo/')
    todolist = Todo.objects.filter(flag=1).filter(user=username)
    finishtodos = Todo.objects.filter(flag=0).filter(user=username)
    return render_to_response('todo/showtodo.html', {'todolist': todolist,'finishtodos': finishtodos,'username':username},
                              context_instance=RequestContext(request))