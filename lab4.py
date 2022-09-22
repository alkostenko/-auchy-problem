from matplotlib import pyplot as plt


#Task 1
#1
y0=-2
a=0.4
h=0.2

x=[]
y=[]
for i in range(0,21,2):
    x.append(i/10)
    y.append(0)

y[0]=y0

def f(x, y):
    f=(a*x**2-1)/(y**3+x**2+0.3)
    return f


for i in range(len(y)-1):
    y[i+1]=y[i]+h*f(x[i], y[i])

print(x)
print(y)

#2
y=[]
for i in range(0,21,2):
    y.append(0)

y[0]=y0
k1=[]
k2=[]
k3=[]

for i in range(len(y)-1):
    k1.append(f(x[i],y[i])*h)
    k2.append(f(x[i]+h/2, y[i]+k1[i]/2)*h)
    k3.append(f(x[i]+h, y[i]+2*k2[i]-k1[i])*h)
    y[i+1]=y[i]+(1/6)*(k1[i]+4*k2[i]+k3[i])

print(y)


#Task2
a=1.65
b=2.01
c=1.25
d=0.71
x0=2.92
y0=1.92
e=10**(-3)
h=0.15
t=[11]
y=[y0]
x=[x0]
k1=[]
k2=[]
k3=[]
k4=[]
q1=[]
q2=[]
q3=[]
q4=[]

def fx(t,x,y):
    return (a*x-b*x*y)

def fy(t,x,y):
    return (-c*y+d*x*y)

for i in range(int(30/h)):
    t.append(0)
    x.append(0)
    y.append(0)

for i in range(int(30/h)):

    t[i+1]=round(t[i]+h,2)

    k1.append(h*fy(t[i],x[i],y[i]))
    q1.append(h*fx(t[i], x[i], y[i]))

    k2.append(h*fy(t[i]+h/2, x[i]+q1[i]/2, y[i]+k1[i]/2))
    q2.append(h*fx(t[i]+h/2, x[i]+q1[i]/2, y[i]+k1[i]/2))

    k3.append(h*fy(t[i]+h/2, x[i]+q2[i]/2, y[i]+k2[i]/2))
    q3.append(h*fx(t[i]+h/2, x[i]+q2[i]/2, y[i]+k2[i]/2))

    k4.append(h*fy(t[i]+h, x[i]+q3[i], y[i]+k3[i]))
    q4.append(h*fx(t[i]+h, x[i]+q3[i], y[i]+k3[i]))

    y[i+1]=y[i]+(1/6)*(k1[i]+2*k2[i]+2*k3[i]+k4[i])
    x[i+1]=x[i]+(1/6)*(q1[i]+2*q2[i]+2*q3[i]+q4[i])


fig, ax=plt.subplots(figsize=(8,6))
ax=plt.plot(t, x, color="green", label="Популяція здобичі")
ax=plt.plot(t, y, color="red", label="Популяція хижаків")

plt.legend()
plt.show()

ax=plt.plot(x,y, color="blue", label="Фазова крива")
ax=plt.scatter(x[0], y[0], label="Початковий стан")
ax=plt.scatter(c/d, a/b, label="Критична точка")

plt.legend()
plt.show()