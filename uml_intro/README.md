# UML Intro — Library Loan System

Modélisation d'un système de prêt de bibliothèque : la structure via un
diagramme de classes, le comportement via un diagramme de séquence.
Format : Mermaid (`.mmd`). Types d'attributs : conventions Python.

---

## 0-class_diagram.mmd

Structure du système : 4 classes, aucune hiérarchie (ni héritage ni interface).

| Classe | Attributs | Méthodes |
|---|---|---|
| `Library` | — | `add_book()`, `register_user()`, `create_loan()` |
| `Book` | `title: str`, `author: str`, `state: bool` | `mark_as_unavailable()`, `mark_as_available()` |
| `User` | `name: str`, `email: str` | — |
| `Loan` | `start_date: str`, `end_date: str` | `close_loan()` |

Relations et multiplicités :

- `Library "1" *-- "0..*" Book` / `User` / `Loan` — composition
- `Loan "0..*" --> "1" Book` — association dirigée
- `Loan "0..*" --> "1" User` — association dirigée

Justification :

- Composition depuis `Library` : supprimer la bibliothèque supprime sa collection, ses membres et ses prêts.
- Association de `Loan` vers `Book`/`User` : fermer un prêt ne détruit ni le livre ni l'utilisateur.
- `1` côté `Book`/`User` : un prêt ne peut exister sans eux. `0..*` côté `Loan` : un livre peut n'avoir jamais été prêté.
- `User` n'a aucune méthode : l'énoncé ne lui attribue aucun comportement.
- `state` conserve le nom exact de l'énoncé (et non `available`).

---

## 1-sequence_diagram.mmd

Comportement : cas d'utilisation « un utilisateur emprunte un livre ».

Participants déclarés à l'ouverture : `User`, `Library`, `Book`.
`Loan` n'est pas déclaré — il apparaît via `create participant Loan`, au moment
exact de sa création.

Flux (4 messages) :

1. `User->>Library: create_loan()` — l'utilisateur initie la demande
2. `Library->>Book: mark_as_unavailable()` — le livre change son propre état
3. `Library->>Loan: Loan(start_date, end_date)` — instanciation du prêt
4. `Library-->>User: loan created` — retour de confirmation

Justification :

- `Library` orchestre : elle porte `create_loan()` et instancie le `Loan`,
  ce qui correspond à la composition `Library *-- Loan` du diagramme de classes.
- `Book` est responsable de sa propre disponibilité : `mark_as_unavailable()`
  est appelée sur `Book`, pas exécutée par `Library`.
- Le livre est rendu indisponible avant la création du prêt.
- Contrainte Mermaid : `create participant` doit être immédiatement suivi d'un
  message dont le participant créé est le destinataire, sinon le rendu échoue.
- Seule la dernière flèche est en pointillés (`-->>`), les appels sont en `->>`.
- Aucun message de retour depuis `Book` : l'énoncé interdit tout message
  supplémentaire.

---

**Auteur** : Mathieu Bailliez
**Dépôt** : `holbertonschool-sw_design_architecture` — dossier `uml_intro`
