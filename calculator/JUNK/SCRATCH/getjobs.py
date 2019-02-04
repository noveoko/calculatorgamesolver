jobs = [a.replace("\n","") for a in open('SCRATCH/jobs.html').read().split("VM441:2 Job Title") if 'United Kingdom' in a]

with open('SCRATCH/jobs_applied_to.txt','w') as outfile:
    outfile.write("Role\tCompany\tLocation\tDate\n")
    for job in jobs:
        role = job.split("Company")[0].strip()
        company = job.split("Company")[1].split("Job Location")[0].replace("Name","")
        location = job.split("Company")[1].split("Job Location")[1].replace("Job Location","")
        applied = job.split("Company")[1].split("Job Location")[-1].split("Applied:")[-1].replace("Applied","")
        outfile.write(f"{role}\t{company}\t{location}\t{applied}\n")
