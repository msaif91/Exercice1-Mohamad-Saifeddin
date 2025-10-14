# main.py
from controllers.task_controller import TaskController
from views.cli import CLIView

def main():
    controller = TaskController()
    view = CLIView()

    while True:
        view.show_menu()
        choix = view.get_input("👉 Choix : ")

        if choix == "1":
            title = view.get_input("Titre de la tâche : ")
            description = view.get_input("Description (facultative) : ")
            task = controller.add_task(title, description)
            print(f"Tâche ajoutée : {task}")

        elif choix == "2":
            view.show_tasks(controller.list_tasks())

        elif choix == "3":
            task_id = int(view.get_input("ID de la tâche à terminer : "))
            if controller.mark_completed(task_id):
                print("✅ Tâche FINIE !")
            else:
                print("❌ Tâche INTROUVABLE !")

        elif choix == "4":
            task_id = int(view.get_input("ID de la tâche à supprimer : "))
            if controller.delete_task(task_id):
                print("🗑️ La tâche supprimée !")
            else:
                print("❌ La tâche estintrouvable.")

        elif choix == "5":
            print("👋 Bye !")
            break
        else:
            print("Choix invalide, réessaie.")

if __name__ == "__main__":
    main()