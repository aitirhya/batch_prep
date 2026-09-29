#!/usr/bin/env python
# coding: utf-8

# In[5]:


import os
from rdkit import Chem

input_folder = r"C:\Users\admin\Desktop\PAich"  
output_file = "batch2.sdf"  

output_path = os.path.join(input_folder, output_file)

sdf_files = [f for f in os.listdir(input_folder) if f.endswith(".sdf") and f.startswith("P") and f != output_file]
sdf_files.sort()  

writer = Chem.SDWriter(output_path)

mol_count = 0

for index in range(0,5):
    sdf_file = sdf_files[index]
    sdf_path = os.path.join(input_folder, sdf_file)
    print(f"[{index+1}] Reading: {sdf_file}")
    
    try:
        suppl = Chem.SDMolSupplier(sdf_path)
        for mol in suppl:
            if mol is not None:
                writer.write(mol)
                mol_count += 1
    except Exception as e:
        print(f"❌ Failed to read {sdf_file}: {e}")

writer.close()

print(f"🧪 Total molecules written: {mol_count}")
print(f"📄 Output saved to: {output_path}")


# In[ ]:





# In[ ]:




