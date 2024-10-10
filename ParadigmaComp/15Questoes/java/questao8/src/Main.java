import java.util.ArrayList;
import java.util.List;

class Empregado {
    String nome;
    String cargo;
    double salario;

    Empregado(String nome, String cargo, double salario) {
        this.nome = nome;
        this.cargo = cargo;
        this.salario = salario;
    }
}

class Empresa {
    String nome;
    List<Empregado> empregados;

    Empresa(String nome) {
        this.nome = nome;
        this.empregados = new ArrayList<>();
    }

    void adicionarEmpregado(Empregado empregado) {
        empregados.add(empregado);
    }

    void exibirEmpregados() {
        for (Empregado empregado : empregados) {
            System.out.println("Nome: " + empregado.nome + ", Cargo: " + empregado.cargo + ", Salário: " + empregado.salario);
        }
    }
}

public class Main {
    public static void main(String[] args) {
        Empresa empresa = new Empresa("Tech Corp");
        Empregado empregado1 = new Empregado("Alice", "Desenvolvedora", 5000);
        Empregado empregado2 = new Empregado("Bob", "Gerente", 7000);

        empresa.adicionarEmpregado(empregado1);
        empresa.adicionarEmpregado(empregado2);

        empresa.exibirEmpregados();
    }
}
