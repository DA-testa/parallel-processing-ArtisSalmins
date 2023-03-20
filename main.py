# python3

def parallel_processing(n, m, data: list):
    output = []

    threads = []

    for t in range(n):
        threads.append(0)
    
    time = 0
    jobs = data
    while(jobs):
        for idt, t in enumerate(threads):
            threads[idt]-=1
            if(threads[idt] <= 0):
                threads[idt] = jobs.pop(0)
                # output.append(f"{idt} {time}")
                output.append((idt, time))
        time+=1

    return output

def main():
    n, m = map(int, input()[:-2].split())

    data = list(map(int, input().split()))

    result = parallel_processing(n,m,data)
    
    for job in result:
        print(f"{job[0]} {job[1]}")

if __name__ == "__main__":
    main()