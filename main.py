from leanlibrary import LeanAgent

def main():
    url = "https://github.com/durant42040/lean4-example"
    commit = "431b4a223095a5ea2d7d3761e6c50d14a87392c3"

    agent = LeanAgent()

    agent.process_repository(url, commit)

    agent.train()
    agent.evaluate()
    agent.prove()



if __name__ == "__main__":
    main()
