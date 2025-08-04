from leanlibrary import LeanAgent

def main():
    url = "https://github.com/durant42040/lean4-example"
    commit = "7d55fefc8822c79c4fc800b3141ed24c5e9644c8"

    agent = LeanAgent()

    agent.process_repository(url, commit)
    agent.prove()



if __name__ == "__main__":
    main()
