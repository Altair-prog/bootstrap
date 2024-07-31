from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def index():
    html = '''
    <!doctype html>
    <html lang="en">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <meta name="description" content="">
        <meta name="generator" content="Hugo 0.84.0">
        <title>Catalog</title>
        <!-- Bootstrap core CSS -->
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet"
              integrity="sha384-9ndCyUaIbzAi2FUVXJi0CjmCapSmO7SnpJef0486qhLnuZ2cdeRhO02iuK6FUUVM" crossorigin="anonymous">
    </head>
    <body>
    <main class="container mt-5">
        <div class="row">
            <!-- Product Card -->
            <div class="col-md-6">
                <div class="card">
                    <img src="https://via.placeholder.com/150" class="card-img-top" alt="Product Image">
                    <div class="card-body">
                        <h5 class="card-title">Product Name</h5>
                        <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
                        <button class="btn btn-success">Купить</button>
                    </div>
                </div>
            </div>
            <!-- Form -->
            <div class="col-md-6">
                <form>
                    <div class="mb-3">
                        <label for="name" class="form-label">Имя</label>
                        <input type="text" class="form-control" id="name" placeholder="Введите ваше имя">
                    </div>
                    <div class="mb-3">
                        <label for="email" class="form-label">Email</label>
                        <input type="email" class="form-control" id="email" placeholder="Введите ваш email">
                    </div>
                    <button type="submit" class="btn btn-primary">Отправить</button>
                </form>
            </div>
        </div>

        <!-- FAQ Section -->
        <div class="mt-5">
            <h4>FAQ</h4>
            <div class="accordion" id="faqAccordion">
                <div class="accordion-item">
                    <h2 class="accordion-header" id="headingOne">
                        <button class="accordion-button" type="button" data-bs-toggle="collapse" data-bs-target="#collapseOne" aria-expanded="true" aria-controls="collapseOne">
                            Как купить?
                        </button>
                    </h2>
                    <div id="collapseOne" class="accordion-collapse collapse show" aria-labelledby="headingOne" data-bs-parent="#faqAccordion">
                        <div class="accordion-body">
                            Здесь будет информация о том, как купить товар.
                        </div>
                    </div>
                </div>
                <div class="accordion-item">
                    <h2 class="accordion-header" id="headingTwo">
                        <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#collapseTwo" aria-expanded="false" aria-controls="collapseTwo">
                            Как доставить?
                        </button>
                    </h2>
                    <div id="collapseTwo" class="accordion-collapse collapse" aria-labelledby="headingTwo" data-bs-parent="#faqAccordion">
                        <div class="accordion-body">
                            Здесь будет информация о доставке.
                        </div>
                    </div>
                </div>
                <div class="accordion-item">
                    <h2 class="accordion-header" id="headingThree">
                        <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#collapseThree" aria-expanded="false" aria-controls="collapseThree">
                            Какая гарантия?
                        </button>
                    </h2>
                    <div id="collapseThree" class="accordion-collapse collapse" aria-labelledby="headingThree" data-bs-parent="#faqAccordion">
                        <div class="accordion-body">
                            Здесь будет информация о гарантии.
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </main>

    <!-- Bootstrap core JS -->
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.6/dist/umd/popper.min.js" integrity="sha384-oBqDVmMz4fnFO9NH3kM4hfDPR2zR5WcF2r9aT1q3CMU62f5zE5bV3Fz2B5xEm0Fw" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.min.js" integrity="sha384-xpG84gfP4gdPtZpwyAi2N8so2l8Z0aP1LfN9XwQ5R9YZ8tpjef5sVscF5k3s8T3J" crossorigin="anonymous"></script>
    </body>
    </html>
    '''
    return render_template_string(html)

if __name__ == '__main__':
    app.run(debug=True)
