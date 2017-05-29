from sklearn.ensemble import ExtraTreesClassifier
import numpy as np
from sklearn.feature_selection import SelectFromModel
import pandas as pd
X,y=pd.read_csv("Dataset.csv"),pd.read_csv("result.csv")
f=[]
f=["P_Amount","MaxMindIPRiskScore","AnonymousProxy","MaxMindBinMatch","MaxMindCountryMatch","MaxMindDistance","MaxMindShipForward","MaxMindHighRiskCountry","FreeMail","3D_SecureStatus","A_Registration_Source","A_Suspicious0te","A_Photo_ID","L_Status","PaymentRequestAmount","ECICode_3D","AcquirerResponseDescription","A_Total_Count_OPA_Payments","A_Total_OPA_Payments_Amount_USD","A_Total_Count_Payment_Request_Loaders","A_Total_Count_Payment_Requests"]
clf = ExtraTreesClassifier()
clf = clf.fit(X, y.values.ravel())
a = clf.feature_importances_  
print len(f)
b = sorted(range(len(a)),key=lambda x:a[x],reverse=True)
print b
for i in range(len(b)):
	print f[b[i]]
