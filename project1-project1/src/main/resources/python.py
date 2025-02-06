import random


def generate_project_name():
    """Generate a random project name"""
    random_number = random.randint(9, 99999)
    project_name = "robot_project_" + str(random_number)
    return project_name


def generate_artifact_name():
    """Generate a random artifact name"""
    random_number = random.randint(9, 99999)
    artifact_name = "robot_artifact_" + str(random_number)
    return artifact_name

def generate_sandbox_name():
    """Generate a random sandbox name"""
    random_number = random.randint(9, 99999)
    artifact_name = "robot_sandbox_" + str(random_number)
    return artifact_name
    
def generate_checkpoint_name():
    """Generate a random checkpoint name"""
    random_number = random.randint(9, 99999)
    checkpoint_name = "robot_checkpoint_" + str(random_number)
    return checkpoint_name  

def generate_random_name():
    """Generate a random name"""
    random_number = random.randint(9, 99999)
    random_name = "robot_" + str(random_number)
    return random_name  

def get_list_from_file(file_path):
    """Read data from a file and return it as a list"""
    with open(file_path, 'r') as file:
        data = file.read().splitlines()
    return data
