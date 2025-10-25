from __future__ import annotations

from stages import Lead
from repo import LeadRepository

class CRMApp:
    """
    Interface simples de linha de comando.
    Mantida apenas com as operações existentes (adicionar e listar).
    """
    def __init__(self, repo: LeadRepository | None = None) -> None:
        self.repo = repo or LeadRepository()

    def add_flow(self) -> None:
        name = input("Nome: ").strip()
        company = input("Empresa: ").strip()
        email = input("E-mail: ").strip()

        if not name or not email or "@" not in email:
            print("Nome e e-mail válido são obrigatórios.")
            return

        try:
            lead = Lead(name=name, company=company, email=email)
            self.repo.add_lead(lead)
            print("✔ Lead adicionado!")
        except ValueError as e:
            print(f"Erro: {e}")

    def list_flow(self) -> None:
        leads = self.repo.list_leads()
        if not leads:
            print("Nenhum lead ainda.")
            return

        print("\n# | Nome                 | Empresa            | E-mail")
        print("--+----------------------+-------------------+-----------------------")
        for i, ld in enumerate(leads, start=1):
            print(f"{i:2d}| {ld.name:<20} | {ld.company:<17} | {ld.email:<23}")

    @staticmethod
    def _menu() -> None:
        print("\nMini-CRM (POO)")
        print("[1] Adicionar lead")
        print("[2] Listar leads")
        print("[0] Sair")

    def run(self) -> None:
        while True:
            self._menu()
            op = input("Escolha: ").strip()
            if op == "1":
                self.add_flow()
            elif op == "2":
                self.list_flow()
            elif op == "0":
                print("Até mais!")
                break
            else:
                print("Opção inválida.")

def main() -> None:
    CRMApp().run()

if __name__ == "__main__":
    main()
