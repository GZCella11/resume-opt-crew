#!/usr/bin/env python
import sys
import warnings

from crew import ResumeCrew

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

def run():
    """
    Run the resume optimization crew.
    """
    inputs = {
        'job_url': 'https://www.linkedin.com/jobs/view/4190362531/?alternateChannel=search&refId=Kh5C%2FsGZJNjvu2mgV6IHDA%3D%3D&trackingId=Pf8Tcbw9s9anmJZXptJmEA%3D%3D',
        'company_name': 'Peregrine Energy Solutions, LLC'
    }
    ResumeCrew().crew().kickoff(inputs=inputs)

if __name__ == "__main__":
    run()
