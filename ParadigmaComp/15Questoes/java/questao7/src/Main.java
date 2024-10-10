import java.util.ArrayList;
import java.util.List;

class Professor {
    String nome;
    List<Escola> escolas;

    Professor(String nome) {
        this.nome = nome;
        this.escolas = new ArrayList<>();
    }

    void adicionarEscola(Escola escola) {
        escolas.add(escola);
    }
}

class Escola {
    String nome;
    List<Professor> professores;

    Escola(String nome) {
        this.nome = nome;
        this.professores = new ArrayList<>();
    }

    void adicionarProfessor(Professor professor) {
        professores.add(professor);
        professor.adicionarEscola(this);
    }
}

public class Main {
    public static void main(String[] args) {
        Escola escola1 = new Escola("Escola A");
        Professor professor1 = new Professor("Dr. João");

        escola1.adicionarProfessor(professor1);
    }
}
