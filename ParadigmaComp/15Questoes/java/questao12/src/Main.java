class Produto {
    double preco;

    Produto(double preco) {
        this.preco = preco;
    }

    // Método de conveniência para somar preços de dois produtos
    public Produto somarPrecos(Produto outroProduto) {
        return new Produto(this.preco + outroProduto.preco);
    }

    @Override
    public String toString() {
        return "Preço total: R$ " + preco;
    }
}

public class Main {
    public static void main(String[] args) {
        Produto produto1 = new Produto(100.50);
        Produto produto2 = new Produto(200.75);

        Produto produtoTotal = produto1.somarPrecos(produto2);
        System.out.println(produtoTotal);  // Exibe a soma dos preços dos dois produtos
    }
}
