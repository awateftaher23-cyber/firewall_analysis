import pandas as pd

df=pd.read_csv("firewall_logs.csv")
ip_data=df.groupby('IP')['Data_Transferred'].sum()
ip_top=ip_data.idxmax()
max_data=ip_data.max()
mean_v=df['Failed_Logins'].mean()
std_v=df['Failed_Logins'].std()
malware_ev=df[df['Event_Type']=='Malware']
malware_ev.to_csv('malware_events.csv', index=False)

print(f"رقم الـ IP الذي استهلك أكبر قدر من البيانات هو: {ip_top}\n")
print(f"كمية البيانات المستهلكة: {max_data}\n")
print(f"المتوسط الحسابي لمحاولات الدخول الخاطئة: {mean_v}\n")
print(f"الانحراف المعياري لمحاولات الدخول الخاطئة: {std_v}\n")
print("تم استخراج أحداث الـ Malware بنجاح وحفظها في ملف 'malware_events.csv'\n")
