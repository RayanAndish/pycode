import pandas as pd

# Creating a sample project schedule with tasks, milestones, durations, and start-end dates.
# This data represents tasks from each phase, estimated to fit within the 17-month timeline.

project_data = {
    "Phase": [
        "Phase 1: Analysis and Design", "Phase 1: Analysis and Design",
        "Phase 2: Consensus and Blockchain Development", "Phase 2: Consensus and Blockchain Development",
        "Phase 3: Token Development", "Phase 3: Token Development",
        "Phase 4: DAO Platform Development", "Phase 4: DAO Platform Development",
        "Phase 5: Integration, Testing, and Security", "Phase 5: Integration, Testing, and Security",
        "Phase 6: Documentation and User Training", "Phase 6: Documentation and User Training"
    ],
    "Task": [
        "Requirements Analysis and Feasibility Study", "Define Technical Architecture",
        "Develop Base Blockchain Structure", "Implement Hybrid Consensus Algorithm",
        "Tokenomics Design", "Develop Token Smart Contract",
        "Develop Core DAO Smart Contracts", "Design UX/UI for DAO",
        "System Stress Testing", "Final Integration Testing",
        "Technical Documentation", "User Guides"
    ],
    "Milestone": [
        "Needs Analysis Complete", "Architecture Defined",
        "Blockchain Structure Ready", "Consensus Algorithm Integrated",
        "Tokenomics Finalized", "Token Contract Complete",
        "DAO Contracts Ready", "UI/UX Design Approved",
        "Stress Testing Complete", "Integration Complete",
        "Documentation Finalized", "User Training Complete"
    ],
    "Duration (weeks)": [4, 3, 6, 8, 2, 4, 6, 4, 3, 3, 3, 2],
    "Start Date": [
        "2024-11-01", "2024-12-01", "2025-01-10", "2025-02-20",
        "2025-04-01", "2025-04-15", "2025-05-10", "2025-06-10",
        "2025-08-01", "2025-08-20", "2025-09-15", "2025-10-01"
    ],
    "End Date": [
        "2024-12-01", "2024-12-21", "2025-02-21", "2025-04-15",
        "2025-04-14", "2025-05-12", "2025-06-21", "2025-07-05",
        "2025-08-21", "2025-09-05", "2025-09-30", "2025-10-14"
    ]
}

# Converting to DataFrame
project_schedule_df = pd.DataFrame(project_data)

# Saving as an Excel file
output_path = "D:/projects/DAO-Project.csv"
project_schedule_df.to_excel(output_path, index=False)

output_path