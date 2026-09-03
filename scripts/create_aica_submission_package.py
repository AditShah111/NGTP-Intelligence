import os, shutil

base_dir = r"C:\Users\ajay_\.gemini\antigravity\scratch\ngtp-litigation-engine"
submission_dir = os.path.join(base_dir, "AICA-L2-CA-Adit-Shah-GST-NGTP-Litigation-Engine")

if os.path.exists(submission_dir):
    shutil.rmtree(submission_dir)

os.makedirs(submission_dir, exist_ok=True)

# 1. Subfolders
f_summary = os.path.join(submission_dir, "01_Project_Summary")
f_arch = os.path.join(submission_dir, "02_System_Architecture_and_Prompts")
f_datasets = os.path.join(submission_dir, "03_Sample_Datasets")
f_media = os.path.join(submission_dir, "04_Media_and_Branding")
f_code = os.path.join(submission_dir, "05_Source_Code")

os.makedirs(f_summary, exist_ok=True)
os.makedirs(f_arch, exist_ok=True)
os.makedirs(os.path.join(f_datasets, "Set1_Proceed_Worthy_Retrospective_Cancellation"), exist_ok=True)
os.makedirs(os.path.join(f_datasets, "Set2_Not_Worthy_HOLD_Missing_Transit"), exist_ok=True)
os.makedirs(f_media, exist_ok=True)
os.makedirs(f_code, exist_ok=True)

# 2. Copy Presentations and Documents
shutil.copy(
    os.path.join(base_dir, "public", "AICA_Level_2_Capstone_Problem_Statement.pdf"),
    os.path.join(f_summary, "AICA_Level_2_Capstone_Problem_Statement.pdf")
)
shutil.copy(
    os.path.join(base_dir, "public", "NGTP_13_Step_Verification_Pipeline.pdf"),
    os.path.join(f_arch, "NGTP_13_Step_Verification_Pipeline.pdf")
)
shutil.copy(
    os.path.join(base_dir, "public", "youtube_thumbnail.jpg"),
    os.path.join(f_media, "ICAI_AICA_Level2_YouTube_Thumbnail.jpg")
)

# 3. Copy Dataset 1 Files
set1_src = os.path.join(base_dir, "public", "sample-data", "set1-proceed")
set1_dst = os.path.join(f_datasets, "Set1_Proceed_Worthy_Retrospective_Cancellation")
for fn in os.listdir(set1_src):
    shutil.copy(os.path.join(set1_src, fn), os.path.join(set1_dst, fn))

# 4. Copy Dataset 2 Files
set2_src = os.path.join(base_dir, "public", "sample-data", "set2-hold")
set2_dst = os.path.join(f_datasets, "Set2_Not_Worthy_HOLD_Missing_Transit")
for fn in os.listdir(set2_src):
    shutil.copy(os.path.join(set2_src, fn), os.path.join(set2_dst, fn))

# 5. Copy Source Code (Excluding node_modules and .next)
for item in ["src", "public", "package.json", "tsconfig.json", "tailwind.config.ts", "postcss.config.mjs", "next.config.mjs", "render.yaml", "Dockerfile", ".dockerignore"]:
    src_item = os.path.join(base_dir, item)
    dst_item = os.path.join(f_code, item)
    if os.path.exists(src_item):
        if os.path.isdir(src_item):
            shutil.copytree(src_item, dst_item, ignore=shutil.ignore_patterns("node_modules", ".next", ".git"))
        else:
            shutil.copy(src_item, dst_item)

print("Successfully created structured AICA submission package directory tree!")