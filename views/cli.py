class CLIView:
    @staticmethod
    def show_menu():
        print("\n=== ToDoList CLI ===")
        print("1. Ajouter une tâche")
        print("2. Lister les tâches")
        print("3. Marquer une tâche comme terminée")
        print("4. Supprimer une tâche")
        print("5. Quitter")

    @staticmethod
    def get_input(prompt):
        return input(prompt)

    @staticmethod
    def show_tasks(tasks):
        if not tasks:
            print("Aucune tâche pour le moment.")
        else:
            for task in tasks:
                print(task)