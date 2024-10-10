class ContaBancaria {
    private double saldo;
    private String titular;

    ContaBancaria(String titular, double saldoInicial) {
        this.titular = titular;
        this.saldo = saldoInicial;
    }

    public void depositar(double valor) {
        saldo += valor;
    }

    public void sacar(double valor) {
        if (valor <= saldo) {
            saldo -= valor;
        } else {
            System.out.println("Saldo insuficiente.");
        }
    }

    public double getSaldo() {
        return saldo;
    }
}

public class Main {
    public static void main(String[] args) {
        ContaBancaria conta = new ContaBancaria("João", 1000);
        conta.depositar(500);
        conta.sacar(200);
        System.out.println("Saldo atual: " + conta.getSaldo());
    }
}
