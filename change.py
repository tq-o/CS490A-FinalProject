import pandas as pd

testcsv = pd.read_csv("mtsamples_copy.csv")
# testcsv.replace(to_replace =[" Hospice - Palliative Care", " General Medicine", " Lab Medicine - Pathology", " Cosmetic / Plastic Surgery", " Physical Medicine - Rehab",
# " Allergy / Immunology", " Psychiatry / Psychology", " Radiology", " Hematology - Oncology", " Obstetrics / Gynecology",
# " Dentistry", " Ophthalmology", " Dermatology", " ENT - Otolaryngology", " Podiatry", " Nephrology", " Gastroenterology", " Neurology", " Urology", " Pediatrics - Neonatal", " Cardiovascular / Pulmonary", " Endocrinology", " Rheumatology"],  
#                  value = "medicines",  
#                   inplace = True) 
# testcsv.replace(to_replace =[" Surgery", " Chiropractic", " Bariatrics", " Neurosurgery", " Autopsy", " Orthopedic"],  
#                  value = "surgery",  
#                   inplace = True)   
# testcsv.replace(to_replace =[" Diets and Nutritions", " Sleep Medicine", " Pain Management", " Speech - Language", " IME-QME-Work Comp etc.", " Letters", " Office Notes", " Emergency Room Reports", " Discharge Summary", " SOAP / Chart / Progress Notes", " Consult - History and Phy."],  
#                  value = "other",  
#                   inplace = True) 
# testcsv.to_csv("mtsamples_copy.csv",  
#                   index = False)
print(len(testcsv))
print(testcsv["medical_specialty"].nunique())