import numpy as np
import pandas as pd

def generate_normal_data(n_sample=1000):
    data = {
        "cpu_usage": np.random.uniform(15, 35, n_sample),
        "memory_usage": np.random.uniform(40, 60, n_sample),
        "process_count": np.random.randint(90, 120, n_sample),
        "new_processes": np.random.randint(1, 5, n_sample),
        "file_acces_rate": np.random.randint(10, 20, n_sample)
}

    return pd.DataFrame(data)

def generate_gradual_attack(n_steps=25):
    cpu  = []
    memory = []
    process = []
    new_proc = []
    file_access = []

    for i in range(n_steps):
        if i < 10:
            cpu.append(np.random.uniform(20, 30))
            memory.append(np.random.uniform(45, 55))
            process.append(np.random.randint(95, 110))
            new_proc.append(np.random.randint(2, 4))
            file_access.append(np.random.randint(12, 18))

        elif i < 18:
            cpu.append(np.random.uniform(40, 65))
            memory.append(np.random.uniform(55, 70))
            process.append(np.random.randint(110, 130))
            new_proc.append(np.random.randint(5, 10))
            file_access.append(np.random.randint(20, 35)) 
        
        else:
            cpu.append(np.random.uniform(85, 95))
            memory.append(np.random.uniform(80, 95))
            process.append(np.random.randint(180, 220))
            new_proc.append(np.random.randint(15, 25))
            file_access.append(np.random.randint(50, 80))

    attack_data = pd.DataFrame({
        "cpu_usage": cpu,
        "memory_usage": memory,
        "process_count": process,
        "new_processes": new_proc,
        "file_access_rate": file_access,
})

    return attack_data

if __name__=="__main__":
    normal = generate_normal_data(1000)
    attack = generate_gradual_attack(25)

    normal["label"] = 0
    attack["label"] = 1

    dataset = pd.concat([normal, attack], ignore_index=True)

    dataset.to_csv("endpoint_dataset.csv", index=False)

    print("Dataset generated successfully.")