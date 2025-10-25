from __future__ import annotations

class Lead:
    """Entidade de domínio: Lead do Mini-CRM."""
    def __init__(self, name: str, company: str, email: str):
        if not name:
            raise ValueError("Nome é obrigatório.")
        if not self._email_valido(email):
            raise ValueError("E-mail inválido.")
        self.name = name.strip()
        self.company = (company or "").strip()
        self.email = email.strip()

    @staticmethod
    def _email_valido(email: str) -> bool:
        if not email or "@" not in email:
            return False
        local, _, domain = email.partition("@")
        return bool(local and domain and "." in domain)

    def to_dict(self) -> dict:
        return {
            "name": self.name,
            "company": self.company,
            "email": self.email,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Lead":
        return cls(
            name=data.get("name", ""),
            company=data.get("company", ""),
            email=data.get("email", ""),
        )
