# run.py
# File chạy chính để huấn luyện và đánh giá mô hình

from gmail_ml.preprocessing import load_and_preprocess_data
from gmail_ml.modeling import train_models
from gmail_ml.evaluation import evaluate_all_models, plot_confusion_matrix

def main():
    # Load dữ liệu
    X_train, X_test, y_train, y_test, vectorizer = load_and_preprocess_data()

    # Train model
    models = train_models(X_train, y_train)

    # Evaluate
    results, best_model, best_name = evaluate_all_models(models, X_test, y_test)

    print("\n=== KẾT QUẢ SO SÁNH ===")
    print(results)

    # Vẽ confusion matrix
    plot_confusion_matrix(best_model, X_test, y_test, best_name)

    # Lưu model
    import joblib
    joblib.dump(best_model, "best_model.pkl")
    joblib.dump(vectorizer, "vectorizer.pkl")

    print(f"\nModel tốt nhất: {best_name} đã được lưu!")

if __name__ == "__main__":
    main()
