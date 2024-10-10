abstract class Funcionario {
    abstract double calcularSalario();
}

class FuncionarioHorista extends Funcionario {
    int horasTrabalhadas;
    double valorPorHora;

    FuncionarioHorista(int horasTrabalhadas, double valorPorHora) {
        this.horasTrabalhadas = horasTrabalhadas;
        this.valorPorHora = valorPorHora;
    }

    @Override
    double calcularSalario() {
        return horasTrabalhadas * valorPorHora;
    }
}

class FuncionarioAssalariado extends Funcionario {
    double salarioFixo;

    FuncionarioAssalariado(double salarioFixo) {
        this.salarioFixo = salarioFixo;
    }

    @Override
    double calcularSalario() {
        return salarioFixo;
    }
}

public class Main {
    public static void main(String[] args) {
        FuncionarioHorista horista = new FuncionarioHorista(160, 20);
        FuncionarioAssalariado assalariado = new FuncionarioAssalariado(5000);

        System.out.println("Salário Horista: " + horista.calcularSalario());
        System.out.println("Salário Assalariado: " + assalariado.calcularSalario());
    }
}
