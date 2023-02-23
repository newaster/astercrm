from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required
from .models import User_addon,Usage,Subscription,Sales,Software
from django.contrib.auth.decorators import login_required

from django.db.models import Count
from datetime import datetime, timedelta




def home(request):
	if request.method=='POST':
		u=request.POST['username']
		p=request.POST['password']

		try:
			selUser = authenticate(username=u, password=p)
			#print(selUser)
		except:
			return render(request,'error.html')

		if selUser:
			login(request, selUser)
			uObj = User_addon.objects.get(user__username=request.user)
			if uObj.role == "SA":
				return redirect('lsa/')
			elif uObj.role == "Admin":
				return redirect('ladmin/')

		else:
			return render(request,'error.html')

	return render(request, 'index.html')


@login_required
def admindb(request):
	sa=Sales.objects.filter(usage_id__usage_user=request.user).count()
	sub=Subscription.objects.filter(usage_id__usage_user=request.user).count()

	return render(request,'admindb.html',{'csa':sa,'csub':sub})


@login_required
def sadb(request):
	return render(request,'sadb.html')



def logout_call(request):
	logout(request)
	return redirect('/')

@login_required
def sales_call(request):
	sa=Sales.objects.filter(usage_id__usage_user=request.user)
	return render(request,'sales.html',{'sa':sa})

@login_required
def subscription_call(request):
	results=Subscription.objects.filter(usage_id__usage_user=request.user).values('usage_id__usage_software__name','usage_id__usage_software__id').annotate(count=Count('usage_id__usage_software__name'))

	return render(request,'subscription.html',{'soft':results})

@login_required
def sublist_call(request,id):

	slist=Subscription.objects.filter(usage_id__usage_user=request.user).filter(usage_id__usage_software__id=id)

	return render(request,'sublist.html',{'slist':slist})





# ADMIN CALLS



@login_required
def cadmindb(request,id):
	sa=Sales.objects.filter(usage_id__usage_user__id=id).count()
	sub=Subscription.objects.filter(usage_id__usage_user__id=id).count()

	return render(request,'admindb.html',{'csa':sa,'csub':sub,'userid':id})

@login_required
def csales_call(request,id):
	sa=Sales.objects.filter(usage_id__usage_user__id=id)
	return render(request,'sales.html',{'sa':sa,'userid':id})

@login_required
def csubscription_call(request,id):
	results=Subscription.objects.filter(usage_id__usage_user__id=id).values('usage_id__usage_software__name','usage_id__usage_software__id').annotate(count=Count('usage_id__usage_software__name'))

	return render(request,'subscription.html',{'soft':results,'userid':id})

@login_required
def csublist_call(request,id,id2):

	slist=Subscription.objects.filter(usage_id__usage_user__id=id2).filter(usage_id__usage_software__id=id)

	return render(request,'sublist.html',{'slist':slist})


@login_required
def customer_call(request):
	usr=User.objects.exclude(username=request.user)

	return render(request,'customer_call.html',{'usr':usr})

@login_required
def addsoftware_call(request):
	if request.method=='POST':
		s=request.POST['sname']
		u=request.POST['url']
		f=request.POST['feature']
		m=request.POST['module']

		check=Software.objects.filter(name=s)
		if check:
			print("Phle se hai")
		else:
			soft=Software(name=s,url=u,feature_addon=f,module_addon=m)
			soft.save()
			return redirect('/lsa/')

	return render(request,'addsoftware_call.html')


@login_required
def adduser_call(request):
	if request.method=='POST':
		fname=request.POST['nm1']
		lname=request.POST['nm2']
		email=request.POST['email']
		username1=request.POST['username']
		password=request.POST['pwd']
		mobileno1=request.POST['mobileno']


		company_name=request.POST['cname']
		job_title=request.POST['jtitle']
		industry=request.POST['industry']
		location=request.POST['add']
		discount=request.POST['discount']

		role="Admin"

		check=User.objects.filter(username=username1)

		if check:
			print("phle se hai")
		else:
			u = User(first_name=fname, last_name=lname, username=username1, password=make_password(password), email=email)
			u.save()
			up = User_addon(user=u,mobileno=mobileno1,company_name=company_name,job_title=job_title,industry=industry,discount=discount,role=role)
			up.save()
			return redirect('/lsa/')

	return render(request,'adduser_call.html')

@login_required
def addsubscription_call(request):
	usr=User.objects.exclude(username=request.user)
	soft=Software.objects.all()
	if request.method=='POST':
		plantsmno=request.POST['plantsmno']

		sdate=request.POST['sdate']
		dt_obj = datetime.strptime(sdate, "%Y-%m-%d")
		dt_obj = dt_obj + timedelta(days=365)
		dt_obj = dt_obj.replace(hour=12, minute=0, second=0)
		ldate = dt_obj.strftime("%Y-%m-%d %H:%M:%S")

		suser=request.POST['suser']
		usage_user=User.objects.get(id=suser)
		sname=request.POST['sname']
		usage_software=Software.objects.get(id=sname)
		price=request.POST['price']

		ur=User_addon.objects.get(user=suser)
		dis=ur.discount
		newprice = int(price)-((int(price)*int(dis))/100)

		check=Usage.objects.filter(usage_user__id=suser,usage_software__id=sname)
		check2=Subscription.objects.filter(plant_smno=plantsmno)


		if check:
			print("Usage phle se hai")
		else:
			u=Usage(usage_user=usage_user,usage_software=usage_software)
			u.save()

			if check2:
				print("Subscription phle se hai")
			else:
				s=Subscription(plant_smno=plantsmno,start_date=sdate,end_date=ldate,usage_id=u,price=newprice)
				s.save()
				return redirect('/lsa/')
	return render(request,'addsubscription_call.html',{'usr':usr,'soft':soft})


@login_required
def addsales_call(request):
	usr=User.objects.exclude(username=request.user)
	soft=Software.objects.all()
	if request.method=='POST':
		plantsmno=request.POST['plantsmno']
		sdate=request.POST['sdate']
		suser=request.POST['suser']
		usage_user=User.objects.get(id=suser)
		sname=request.POST['sname']
		usage_software=Software.objects.get(id=sname)
		price=request.POST['price']

		stype=request.POST['stype']

		check=Usage.objects.filter(usage_user__id=suser,usage_software__id=sname)
		check2=Sales.objects.filter(plant_smno=plantsmno)

		ur=User_addon.objects.get(user=suser)
		dis=ur.discount
		newprice = int(price)-((int(price)*int(dis))/100)

		if check:
			print("Usage phle se hai")
		else:
			u=Usage(usage_user=usage_user,usage_software=usage_software)
			u.save()

			if check2:
				print("Sales phle se hai")
			else:
				s=Sales(plant_smno=plantsmno,datetime=sdate,usage_id=u,price=newprice,sales_type=stype)
				s.save()
				return redirect('/lsa/')

	return render(request,'addsales_call.html',{'usr':usr,'soft':soft})